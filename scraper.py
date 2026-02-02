import os
from curl_cffi import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import time
import random
import re

# --- CONFIG ---
OUTPUT_DIR = "offers"
BASE_URL = "https://lowendtalk.com/categories/offers/p"
PAGES_TO_SCAN = 1

# --- PROXY CONFIGURATION ---
PROXY_URL = os.environ.get("PROXY_URL") 
# curl_cffi expects proxies in a specific format
PROXIES = {"http": PROXY_URL, "https": PROXY_URL} if PROXY_URL else None

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title).replace(" ", "_")[:100]

def file_exists(thread_id):
    if not os.path.exists(OUTPUT_DIR): return False
    for file in os.listdir(OUTPUT_DIR):
        if file.startswith(f"{thread_id}_"):
            return True
    return False

def save_markdown(data):
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    filename = f"{OUTPUT_DIR}/{data['id']}_{clean_filename(data['title'])}.md"
    content = f"""---
id: {data['id']}
title: "{data['title']}"
date: "{data['date']}"
author: "{data['author']}"
link: "{data['url']}"
---
# {data['title']}
**Link:** [Original Thread]({data['url']})

{data['body']}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"   ✅ [SAVED] {filename}")

def run_scraper():
    print(f"--- Starting Stealth Scraper (curl_cffi) ---")
    
    # Init Session with Chrome Fingerprint
    # This is the magic line that bypasses Cloudflare
    session = requests.Session(impersonate="chrome120")
    if PROXIES:
        session.proxies = PROXIES
        print(f"🕵️  Proxy Enabled")

    for page in range(1, PAGES_TO_SCAN + 1):
        print(f"\n📄 Scanning Page {page}...")
        try:
            # Fetch Listing
            r = session.get(f"{BASE_URL}{page}", timeout=30)
            soup = BeautifulSoup(r.content, 'html.parser')
            
            threads = soup.find_all('li', class_='ItemDiscussion')
            print(f"   Found {len(threads)} raw items.")

            for thread in threads:
                try:
                    title_tag = thread.select_one('.Title a')
                    if not title_tag: continue

                    link = title_tag['href']
                    title = title_tag.text.strip()
                    thread_id = thread.get('id', '').replace("Discussion_", "")
                    
                    if file_exists(thread_id):
                        print(f"   ⏭️ [SKIP] {thread_id} exists.")
                        continue

                    print(f"   🔎 Processing: {title[:40]}...")
                    
                    # Polite Delay
                    time.sleep(random.uniform(2.0, 5.0))
                    
                    # Fetch Thread Detail
                    thread_resp = session.get(link, timeout=30)
                    
                    # Cloudflare Check
                    if "Just a moment" in thread_resp.text:
                        print("   ❌ STILL BLOCKED. (Consider increasing sleep time)")
                        continue

                    thread_soup = BeautifulSoup(thread_resp.content, 'html.parser')
                    main_post = thread_soup.find('div', class_='Message')
                    
                    # Metadata
                    author_tag = thread.find('span', class_='Author')
                    author = author_tag.text.strip() if author_tag else "Unknown"
                    date_tag = thread.find('time')
                    date = date_tag['datetime'] if date_tag else "Unknown"

                    if main_post:
                        save_markdown({
                            'id': thread_id,
                            'title': title,
                            'url': link,
                            'author': author,
                            'date': date,
                            'body': md(str(main_post))
                        })

                except Exception as e:
                    print(f"   ❌ Error: {e}")

        except Exception as e:
            print(f"Critical Fail: {e}")

if __name__ == "__main__":
    run_scraper()
