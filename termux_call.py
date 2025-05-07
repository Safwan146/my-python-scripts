# Developer: Safwan

print("""
__        __                     
/ _\ __ _ / _|_      ____ _ _ __  
\ \ / _` | |_\ \ /\ / / _` | '_ \ 
_\ \ (_| |  _|\ V  V / (_| | | | |
\__/\__,_|_|   \_/\_/ \__,_|_| |_|
""")
print("Welcome to the Auto Call Script!")

import os

def call_now():
    number = input("Enter phone number: ")
    os.system(f"termux-telephony-call {number}")

if __name__ == "__main__":
    call_now()