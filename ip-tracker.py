import requests

# Color Setup
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def banner():
    ascii_banner = """
  ____         __                     
 / ___|  __ _ / _|_      ____ _ _ __  
 \___ \ / _` | |_\ \ /\ / / _` | '_ \ 
  ___) | (_| |  _|\ V  V / (_| | | | |
 |____/ \__,_|_|   \_/\_/ \__,_|_| |_|
    """
    print(f"{CYAN}{ascii_banner}{RESET}")
    print(f"{GREEN}     IP Tracker by Safwan Al-Sadaf{RESET}")
    print(f"{CYAN}     GitHub: https://github.com/safwanalsadaf{RESET}\n")

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,query,country,regionName,city,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print(f"{CYAN}IP Info for {data['query']}:{RESET}")
        print(f"{GREEN}Country     : {RESET}{data['country']}")
        print(f"{GREEN}Region      : {RESET}{data['regionName']}")
        print(f"{GREEN}City        : {RESET}{data['city']}")
        print(f"{GREEN}ZIP Code    : {RESET}{data['zip']}")
        print(f"{GREEN}Timezone    : {RESET}{data['timezone']}")
        print(f"{GREEN}ISP         : {RESET}{data['isp']}")
        print(f"{GREEN}Org         : {RESET}{data['org']}")
        print(f"{GREEN}AS Info     : {RESET}{data['as']}")
        print(f"{GREEN}Reverse DNS : {RESET}{data['reverse']}")
        print(f"{GREEN}Mobile User : {RESET}{data['mobile']}")
        print(f"{GREEN}Using Proxy : {RESET}{data['proxy']}")
        print(f"{GREEN}Lat/Lon     : {RESET}{data['lat']}, {data['lon']}")
        print(f"{GREEN}Map Link    : {RESET}https://maps.google.com/?q={data['lat']},{data['lon']}")
    else:
        print(f"{RED}[!] Error: {data['message']}{RESET}")

def main():
    banner()
    target_ip = input(f"{GREEN}Enter IP or domain: {RESET}")
    get_ip_info(target_ip)

if __name__ == "__main__":
    main()