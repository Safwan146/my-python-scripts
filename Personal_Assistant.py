import os
import time
import schedule
from datetime import datetime

# ASCII Banner
print("""
__        __                     
/ _\\ __ _ / _|_      ____ _ _ __  
\\ \\ / _` | |_\\ \\ /\\ / / _` | '_ \\ 
_\\ \\ (_| |  _|\\ V  V / (_| | | | |
\\__/\\__,_|_|   \\_/\\_/ \\__,_|_| |_|
""")

# Voice Speak Function using termux-tts-speak
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

# Tasks
def morning_wakeup():
    speak("আব্বু উঠো, তোমার অফিসের সময় হয়ে গেছে, ৯টা বেজে গেছে। উঠো আব্বু উঠো না।")

def breakfast_reminder():
    speak("আব্বু, সকাল ১০টা বাজে। এখন ব্রেকফাস্ট করে নাও।")

def lunch_reminder():
    speak("আব্বু, দুপুর ১টা বাজে। এবার লাঞ্চ করে ফেলো।")

def evening_reminder():
    speak("আব্বু, এখন বিকেল ৪টা। তোমার ছুটির সময়।")

def play_music():
    speak("তুমি বিরক্ত হয়ে আছো, তোমার জন্য গান চালাচ্ছি।")
    os.system("termux-media-player play voice/motivation_song.mp3")

def random_street_food_tip():
    speak("আজ বিকেলে কিছু স্ট্রিট ফুড খেয়ে ফেলো না দোস্ত!")

# Schedule jobs
schedule.every().day.at("09:00").do(morning_wakeup)
schedule.every().day.at("10:00").do(breakfast_reminder)
schedule.every().day.at("13:00").do(lunch_reminder)
schedule.every().day.at("16:00").do(evening_reminder)
schedule.every().day.at("17:00").do(random_street_food_tip)

# Custom command system
def command_mode():
    while True:
        cmd = input("\nতোমার কথা বলো দোস্ত: ").lower()

        if "বিরক্ত" in cmd or "birokto" in cmd:
            play_music()
        elif "গান" in cmd:
            play_music()
        elif "স্ট্রিট ফুড" in cmd:
            random_street_food_tip()
        elif "ঘুম" in cmd:
            morning_wakeup()
        elif "বন্ধু" in cmd:
            speak("আমি সবসময় তোর পাশে আছি দোস্ত।")
        elif "বেরিয়ে যা" in cmd or "exit" in cmd:
            speak("আচ্ছা দোস্ত, দেখা হবে পরে।")
            break
        else:
            speak("এই কমান্ডটা আমি বুঝিনি দোস্ত।")

# Main loop
if __name__ == "__main__":
    speak("তোমার এসিস্ট্যান্ট চালু হয়েছে। Safwan বানিয়েছে এটা।")
    while True:
        schedule.run_pending()
        time.sleep(1)
        now = datetime.now()
        if now.second % 30 == 0:
            print(f"চলছে: {now.strftime('%H:%M:%S')}")
        # Command mode entry shortcut (every 5 minutes)
        if now.minute % 5 == 0 and now.second == 0:
            command_mode()
