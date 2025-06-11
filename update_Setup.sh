#!/bin/bash
# Cyber_protector_Army:BD Professional Termux Ethical Hacking Setup Tool
# Developer: Safwan Al-Sadaf
# Telegram: @Safwan_al_sadaf
# Facebook: https://www.facebook.com/share/15kFDb1uXr/

# Define Colors
RED='\e[1;91m'
GREEN='\e[1;92m'
YELLOW='\e[1;93m'
BLUE='\e[1;94m'
MAGENTA='\e[1;95m'
CYAN='\e[1;96m'
NC='\e[0m' # No Color

# Clear screen
clear

# Custom ASCII Logo
echo -e "${RED}"
echo "____         __                       "
echo "/ ___|  __ _ / _|_      ____ _ _ __    "
echo "\\___ \\ / _\` | |_\\\\ /\\\\ / _\` | '_ \\   "
echo " ___) | (_| |  _|\\\\ V  V / (_| | | | | "
echo "|____/ \\__,_|_|   \\_/\\\\_/ \\__,_|_| |_|"
echo -e "${YELLOW}         Welcome to our Cyber World${NC}"
echo -e "${CYAN}        Developed by Safwan Al-Sadaf"
echo -e "        Telegram: @Safwan_al_sadaf"
echo -e "        Facebook: fb.com/share/15kFDb1uXr\n${NC}"

# Ask for user's name
read -p "Enter your name (for personalization): " USER_NAME

# Main Menu
while true; do
    echo -e "${GREEN}\n=== Main Menu ===${NC}"
    echo "1. Full Setup (All Hacking Tools)"
    echo "2. Install Selected Tools Only"
    echo "3. Update All Packages"
    echo "4. About Developer"
    echo "5. Exit"
    read -p "Choose an option: " choice

    case $choice in
        1)
            echo -e "${YELLOW}\n[+] Starting Full Setup...${NC}"
            pkg update -y && pkg upgrade -y
            pkg install -y python python2 git curl wget nano
            pkg install -y nmap hydra sqlmap metasploit termux-api
            pkg install -y openssh net-tools tor wireshark
            pkg install -y php ruby clang dnsutils
            pip install requests beautifulsoup4 colorama
            echo -e "${GREEN}All tools installed successfully.${NC}"
            ;;
        2)
            echo -e "${CYAN}\n[+] Selected Tools Menu:${NC}"
            echo "   a. Nmap"
            echo "   b. Hydra"
            echo "   c. Sqlmap"
            echo "   d. Metasploit"
            echo "   e. Back"
            read -p "Choose tool to install: " tool_choice
            case $tool_choice in
                a) pkg install -y nmap;;
                b) pkg install -y hydra;;
                c) pkg install -y sqlmap;;
                d) pkg install -y unstable-repo && pkg install -y metasploit;;
                e) continue;;
                *) echo "Invalid option.";;
            esac
            ;;
        3)
            echo -e "${YELLOW}[+] Updating...${NC}"
            pkg update -y && pkg upgrade -y
            echo -e "${GREEN}Update complete.${NC}"
            ;;
        4)
            echo -e "\n${MAGENTA}Developer: Safwan Al-Sadaf"
            echo "Telegram: @Safwan_al_sadaf"
            echo "Facebook: https://www.facebook.com/share/15kFDb1uXr${NC}"
            ;;
        5)
            echo -e "${BLUE}\nGoodbye, $USER_NAME! Stay ethical. 👨‍💻${NC}"
            exit
            ;;
        *)
            echo -e "${RED}Invalid choice. Try again.${NC}"
            ;;
    esac
done
