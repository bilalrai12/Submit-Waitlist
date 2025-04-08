import concurrent.futures
import requests
import json
import random
from urllib.parse import urlencode
import time
import datetime
import threading
from colorama import init, Fore, Style


init(autoreset=True)

threads = 10 # Config threads

accounts = []    
proxies_list = []

proxy_lock = threading.Lock()
global_proxy_index = 0

def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("[%H:%M:%S %d/%m/%Y]")

def log_message(idx, email, message, color=Fore.WHITE):
    print(f"{get_timestamp()} [{idx}] [{email}] {color}{message}{Style.RESET_ALL}")

def get_next_proxy():
    global global_proxy_index
    with proxy_lock:
        proxy = proxies_list[global_proxy_index]
        global_proxy_index = (global_proxy_index + 1) % len(proxies_list)
    return proxy

def get_current_ip(proxy):
    try:
        proxies = {"http": proxy, "https": proxy}
        r = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("ip", "-")
    except Exception:
        return "-"

def random_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Tom", "Lucy", "Peter", "Sophie", "Michael", "Emily"]
    last_names = ["Smith", "Doe", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Taylor"]
    return random.choice(first_names), random.choice(last_names)

def process_account(account, idx):
    email = account["email"]
    password = account["password"]

    assigned_proxy = get_next_proxy()
    account["proxy"] = assigned_proxy
    account["ip"] = get_current_ip(assigned_proxy)
    log_message(idx, email, f" - Current IP: {account['ip']}", Fore.CYAN)

    first_name, last_name = random_name()
    payload = {
        "fields[Contact%20Email]": email,
        "fields[Contact%20Name]": first_name,
        "fields[Contact%20Last%20name]": last_name,
        "name": "Contact 11 Form",
        "pageId": "67e9a27f8336152373dcfccb",
        "elementId": "17e22948-4cba-360d-8f70-66e920d49528",
        "domain": "www.codex.xyz",
        "source": "https://www.codex.xyz/contact",
        "test": "false",
        "dolphin": "false"
    }

    headers_req = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.codex.xyz",
        "Referer": "https://www.codex.xyz/",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }

    api_url = "https://webflow.com/api/v1/form/67d0b0a8a52ef03e7caca863"
    max_retries = 5
    retry_count = 0
    success = False

    encoded_payload = urlencode(payload)

    while retry_count < max_retries and not success:
        try:
            current_proxy = account["proxy"]
            proxies = {"http": current_proxy, "https": current_proxy}
            response = requests.post(api_url, headers=headers_req, data=encoded_payload, proxies=proxies, timeout=15)
            response.raise_for_status()
            log_message(idx, email, f"Successfully submitted waitlist request. Response: {response.text}", Fore.GREEN)
            success = True
        except Exception as ex:
            log_message(idx, email, f"Attempt {retry_count+1} failed: {ex}", Fore.YELLOW)
            retry_count += 1
            new_proxy = get_next_proxy()
            account["proxy"] = new_proxy
            account["ip"] = get_current_ip(new_proxy)
            time.sleep(3)
    if not success:
        log_message(idx, email, "Failed after 5 retries.", Fore.RED)

def main():
    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    accounts.append({
                        "email": parts[0].strip(),
                        "password": parts[1].strip()
                    })
        if not accounts:
            print("No valid accounts found in accounts.txt")
            return
    except Exception as e:
        print(f"Error reading accounts.txt: {e}")
        return

    try:
        with open("proxies.txt", "r", encoding="utf-8") as f:
            global proxies_list
            proxies_list = [line.strip() for line in f if line.strip()]
        if not proxies_list:
            print("No proxies found in proxies.txt")
            return
    except Exception as e:
        print(f"Error reading proxies.txt: {e}")
        return

    print(f"{Fore.MAGENTA}{get_timestamp()} SCRIPT SHARE BY : {len(accounts)} https://t.me/Bilalstudio2 and {len(proxies_list)} {Style.RESET_ALL}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(process_account, account, idx)
                   for idx, account in enumerate(accounts, start=1)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing account: {e}")

if __name__ == "__main__":
    main()
