#!/bin/bash

clear

=== Custom ASCII Logo ===

echo -e "\e[92m


---

/ |  __ _ / |      ____ _ _ __
_ \ / ` | |\ \ /\ / ` | ' \
) | (| |  |\ V  V / (| | | | |
|/ \__,||   \/\/\__,|| ||
\e[0m"

echo -e "\e[96m      ★ Welcome to our Cyber World ★\e[0m" echo -e "\e[90m      Developed by Safwan Al-Sadaf\e[0m" echo -e "\e[90m Telegram: @Safwan_al_sadaf  |  GitHub: Safwan146\e[0m" echo ""

=== Storage Permission Check ===

if [ ! -d "$HOME/storage" ]; then echo -e "\e[93m[✔] Storage permission not found. Requesting now...\e[0m" termux-setup-storage sleep 2 else echo -e "\e[92m[✔] Storage permission already granted.\e[0m" sleep 1 fi

=== Update & Upgrade ===

echo -e "\n\e[96m[→] Updating Termux packages...\e[0m" pkg update -y && pkg upgrade -y

=== Install All Required Packages ===

echo -e "\n\e[96m[→] Installing essential hacking and fun packages...\e[0m" pkg install -y python python2 git curl wget php openssh nmap 
nano hydra tor ruby clang zip unzip figlet toilet 
openssl proot dnsutils tsu termux-api cmatrix libcaca

=== Upgrade pip and install Python libraries ===

echo -e "\n\e[96m[→] Installing Python libraries...\e[0m" pip install --upgrade pip pip install requests mechanize bs4 colorama lolcat

=== Matrix Style Animation ===

echo -e "\n\e[92m[★] Launching Matrix screen (Press CTRL+C to skip)...\e[0m" cmatrix -u 4 -C green & sleep 4 killall cmatrix >/dev/null 2>&1 clear

=== Caca Fire Effect ===

echo -e "\n\e[91m[★] Launching 🔥 ascii fire (Press CTRL+C to skip)...\e[0m" sleep 2 cacafire

=== Final Success Message ===

clear echo -e "\n\n\e[92m[✔] All packages installed successfully!\e[0m" | lolcat echo -e "\e[96m[★] You are now ready to hack the matrix — ethically.\e[0m" | lolcat echo -e "\e[95m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ✅ Setup Completed! ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \e[0m" | lolcat