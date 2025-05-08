import time
import os
import schedule
from datetime import datetime
from termux import TTS

# ASCII Art
ascii_art = """
__        __                     
/ _\ __ _ / _|_      ____ _ _ __  
\ \ / _` | |_\ \ /\ / / _` | '_ \ 
_\ \ (_| |  _|\ V  V / (_| | | | |
\__/\__,_|_|   \_/\_/ \__,_|_| |_|
"""

print(ascii_art)

def play_audio(file_path):
    os.system(f"termux-media-player play {file_path}")

def wake_up_reminder():
    TTS("আব্বু উঠো, তোমার অফিসের সময় হয়ে গেছে। ৯টা বেজে গেছে, উঠো আব্বু উঠোনা।")
    play_audio("voice/abu_uTho.mp3")  # Add path to your audio file

def breakfast_reminder():
    TTS("ব্রেকফাস্ট করো আব্বু, সময় হয়ে গেছে।")

def lunch_reminder():
    TTS("লাঞ্চ করার সময় হয়েছে, ভালো করে খাও।")

def bored_reminder():
    TTS("বিরক্ত লাগতেছে? চল শোনো একটা গান!")
    play_audio("voice/motivation_song.mp3")  # Replace with your desired audio file

def street_food_reminder():
    TTS("স্ট্রীট ফুড খাওয়ার কথা মনে আছে তো?")

# Scheduling Tasks
schedule.every().day.at("09:00").do(wake_up_reminder)
schedule.every().day.at("10:00").do(breakfast_reminder)
schedule.every().day.at("13:00").do(lunch_reminder)
schedule.every().day.at("16:00").do(street_food_reminder)
schedule.every().day.at("17:00").do(bored_reminder)  # Change based on mood

while True:
    schedule.run_pending()
    time.sleep(60)