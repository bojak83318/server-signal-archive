import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import time
import random
import re

# --- CONFIG ---
OUTPUT_DIR = "offers"
BASE_URL = "https://lowendtalk.com/categories/offers/p"
PAGES_TO_SCAN = 3 

# Professional Headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# --- PROXY CONFIGURATION (The "Secret" Tunnel) ---
PROXY_URL = os.environ.get("PROXY_URL") 
PROXIES = { "http": PROXY_URL, "https": PROXY_URL } if PROXY_URL else None

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title).replace(" ", "_")[:50]

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
    print(f"   [SAVED] {filename}")

def run_scraper():
    print(f"--- Starting Git-Scraper Job ---")
    if PROXIES:
        print(f"🕵️  Using Proxy: ENABLED (Routing via Romania)")
    else:
        print(f"⚠️  Using Proxy: DISABLED (Direct Connection)")

    for page in range(1, PAGES_TO_SCAN + 1):
        print(f"Scanning Page {page}...")
        try:
            r = requests.get(f"{BASE_URL}{page}", headers=HEADERS, proxies=PROXIES, timeout=15)
            if r.status_code != 200:
                print(f"!! Blocked/Error on Page {page}: {r.status_code}")
                break
                
            soup = BeautifulSoup(r.content, 'html.parser')
            threads = soup.find_all('li', class_='ItemDiscussion')

            for thread in threads:
                try:
                    title_tag = thread.find('a', class_='Title')
                    link = title_tag['href']
                    title = title_tag.text.strip()
                    thread_id = thread['id'].replace("Discussion_", "")
                    
                    if file_exists(thread_id):
                        print(f"   [SKIP] {thread_id} exists.")
                        continue

                    print(f"-> New Offer: {title[:30]}...")
                    # Respectful delay before fetching detail
                    time.sleep(random.uniform(1.5, 3.0))
                    
                    thread_resp = requests.get(link, headers=HEADERS, proxies=PROXIES, timeout=15)
                    thread_soup = BeautifulSoup(thread_resp.content, 'html.parser')
                    
                    main_post = thread_soup.find('div', class_='Message')
                    author = thread.find('span', class_='Author').text.strip()
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
                    print(f"   Error parsing thread: {e}")

        except Exception as e:
            print(f"Critical Fail on Page {page}: {e}")

if __name__ == "__main__":
    run_scraper()
