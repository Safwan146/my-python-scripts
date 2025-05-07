import os
import time

def banner():
    os.system("clear")
    print(r"""
__        __                     
/ _\ __ _ / _|_      ____ _ _ __  
\ \ / _` | |_\ \ /\ / / _` | '_ \ 
_\ \ (_| |  _|\ V  V / (_| | | | |
\__/\__,_|_|   \_/\_/ \__,_|_| |_|
""")
    print("\033[1;36m----------------------------------------\033[0m")
    print("\033[1;33m  Termux Auto Setup Script\033[0m")
    print("\033[1;32m  Developed By : Safwan\033[0m")
    print("\033[1;36m----------------------------------------\033[0m\n")
    time.sleep(1)

def install_packages(packages):
    for package in packages:
        print(f"\033[1;34m[*] Installing {package}...\033[0m")
        os.system(f"pkg install {package} -y > /dev/null")
        print(f"\033[1;32m[✓] {package} installed!\033[0m\n")
        time.sleep(0.2)

def finished():
    os.system("cowsay 'Setup Complete!' | lolcat")
    os.system("sl")  # Little animation

def main():
    os.system("termux-setup-storage")
    os.system("pkg update -y > /dev/null")
    os.system("pkg upgrade -y > /dev/null")

    banner()

    packages = [
        "python", "python2", "git", "figlet", "toilet", "cowsay", "ruby", "nano",
        "curl", "wget", "php", "nmap", "openssh", "bash", "clang", "zip", "unzip",
        "sl", "lolcat"
    ]

    install_packages(packages)
    finished()

if __name__ == "__main__":
    main()