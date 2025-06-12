#!/bin/bash

clear
echo -e "\e[1;32m"
cat << "EOF"
  ____         __                       
 / ___|  __ _ / _|_      ____ _ _ __    
 \___ \ / _` | |_ \ \ /\ / / _` | '_ \   
  ___) | (_| |  _| \ V  V / (_| | | | |  
 |____/ \__,_|_|    \_/\_/ \__,_|_| |_| 
EOF
echo -e "\e[0m"

echo ""
echo -e "\e[1;36m★ Welcome to our Cyber World ★\e[0m"
echo ""
echo -e "\e[1;33mDeveloped by Safwan Al-Sadaf\e[0m"
echo -e "\e[1;34mTelegram: @Safwan_al_sadaf  |  GitHub: Safwan146\e[0m"
echo ""
echo "======================================="

# Get storage permission
termux-setup-storage

# Update & upgrade
pkg update -y && pkg upgrade -y

# Install core hacking-related packages
pkg install -y python python2 git curl wget php openssh nmap hydra netcat tsu \
tor dnsutils nano vim neofetch htop clang zip unzip tar \
toilet figlet ruby libcaca

# Install Ruby-based tools
gem install lolcat

# Show system info
echo ""
neofetch | lolcat

# Done message
echo ""
echo "======================================="
echo -e "\e[1;32mSetup Complete! You're ready for Ethical Hacking with Termux!\e[0m"
echo -e "\e[1;36mFollow: @Safwan_al_sadaf for more tools & updates.\e[0m"
echo "======================================="