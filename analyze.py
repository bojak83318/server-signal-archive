import os
import re
import csv

INPUT_DIR = "offers"
OUTPUT_FILE = "glm4_candidates.csv"

# --- GLM-4 HARDWARE SPECS ---
# We strictly want High-IPC cores with AVX-512 capability
VALID_CPUS = [
    "EPYC", "Ryzen", "Threadripper", 
    "Xeon Gold", "Xeon Platinum", "Xeon W"
]
MIN_RAM_GB = 16

def extract_specs(text):
    specs = {"ram": 0, "cpu": "Unknown", "price": "Unknown"}
    
    # 1. RAM Logic: Look for "16GB", "32 GB", etc.
    # Exclude massive numbers > 512 (likely storage)
    ram_matches = re.findall(r'(\d+)\s*(?:GB|GiB)\s*(?:RAM|Memory|DDR)', text, re.IGNORECASE)
    if not ram_matches:
        # Fallback: look for just "16GB" if context is tight
        ram_matches = re.findall(r'(\d+)\s*(?:GB|GiB)', text, re.IGNORECASE)
    
    if ram_matches:
        valid_rams = [int(x) for x in ram_matches if 16 <= int(x) < 512]
        if valid_rams:
            specs["ram"] = max(valid_rams)

    # 2. CPU Logic
    for cpu in VALID_CPUS:
        if re.search(cpu, text, re.IGNORECASE):
            specs["cpu"] = cpu
            # Try to capture model number (e.g. "EPYC 9655")
            model = re.search(f"({cpu}\s*[\w-]+)", text, re.IGNORECASE)
            if model: specs["cpu"] = model.group(1)
            break
            
    # 3. Price Logic
    price_match = re.search(r'([$€£]\s*\d+(?:\.\d{2})?)', text)
    if price_match:
        specs["price"] = price_match.group(1)
        
    return specs

def analyze():
    print("--- Running Deterministic Analysis ---")
    if not os.path.exists(INPUT_DIR): 
        print("No offers directory found.")
        return
    
    candidates = []
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".md")]
    
    for f in files:
        with open(os.path.join(INPUT_DIR, f), 'r', encoding="utf-8") as file:
            content = file.read()
            specs = extract_specs(content)
            
            # THE FILTER: Must meet GLM-4 Spec
            if specs["ram"] >= MIN_RAM_GB and specs["cpu"] != "Unknown":
                candidates.append({
                    "File": f,
                    "CPU": specs["cpu"],
                    "RAM": specs["ram"],
                    "Price": specs["price"]
                })
    
    # Sort by RAM (Highest First)
    candidates.sort(key=lambda x: x["RAM"], reverse=True)
    
    if candidates:
        with open(OUTPUT_FILE, 'w', newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["CPU", "RAM", "Price", "File"])
            writer.writeheader()
            writer.writerows(candidates)
        print(f"✅ Analysis Complete. Found {len(candidates)} candidates.")
    else:
        print("⚠️ No suitable candidates found yet.")

if __name__ == "__main__":
    analyze()
