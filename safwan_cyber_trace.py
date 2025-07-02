import os
import time

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def main_menu():
    clear()
    print(" ------------------------------------------------------")
    print("🧑‍💻 Developer: Safwan Al-Sadaf  ")
    print("💬 Telegram: @Safwan_al_sadaf  ")
    print("🎯 Mission: Educating the public on cyber safety and helping trace the roots of cybercrime.")
    print("_____________________________________")
    print()
    print("🔰 Tool: Safwan Cyber Trace  ")
    print("📅 Version: 1.0.0  ")
    print("🌐 Facebook: facebook.com/share/15kFDb1uXr/")
    print()
    print("📌 With this tool, you can analyze phishing links, trace IPs, check hosting & WHOIS information, and detect source code leaks.")
    print("----------------------------------------------------------")
    print()
    print("Please choose an option:  ")
    print("[1] Analyze Phishing Link  ")
    print("[2] Trace IP Location  ")
    print("[3] Hosting & WHOIS Information  ")
    print("[4] Source Code Leak Check  ")
    print("[0] Exit Tool  ")
    print()

    option = input("🔎 Enter your option (0-4): ")

    if option == "1":
        phishing_link = input("                                                                                        🔗 Enter the phishing link: ")
        print(f"\nAnalyzing the link: {phishing_link}")
        time.sleep(1)
        print("⚠️ (Demo only. Real analysis feature to be added.)")

    elif option == "2":
        ip = input("                                                                                        🌐 Enter the IP address: ")
        print(f"\nTracing IP: {ip}")
        time.sleep(1)
        print("📍 (Demo only. IP trace coming soon.)")

    elif option == "3":
        domain = input("                                                                                        🧩 Enter the domain name: ")
        print(f"\nFetching WHOIS info for: {domain}")
        time.sleep(1)
        print("🗂️ (Demo only. WHOIS feature coming soon.)")

    elif option == "4":
        url = input("                                                                                        💻 Enter URL to check for code leak: ")
        print(f"\nScanning for source code leaks at: {url}")
        time.sleep(1)
        print("🔐 (Demo only. Leak detection module coming soon.)")

    elif option == "0":
        print("\n👋 Exiting... Stay safe online!")

    else:
        print("\n❌ Invalid option. Please enter 0-4.")

if __name__ == "__main__":
    main_menu()