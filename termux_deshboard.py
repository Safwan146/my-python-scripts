import os
import time

# Color codes
colors = {
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "cyan": "\033[1;36m",
    "reset": "\033[0m",
    "white": "\033[1;37m"
}

# Banner function
def show_banner():
    os.system("clear")
    os.system("figlet Termux Setup | lolcat")
    print(colors["cyan"] + "----------------------------------------" + colors["reset"])
    print(colors["yellow"] + "    Welcome to Termux Dashboard" + colors["reset"])
    print(colors["green"] + "    Developed by: " + colors["white"] + "Safwan" + colors["reset"])
    print(colors["cyan"] + "----------------------------------------\n" + colors["reset"])

# Color selection menu
def choose_color():
    print(colors["white"] + "Choose a color for your name:")
    for i, c in enumerate(["red", "green", "yellow", "blue", "cyan"], start=1):
        print(f"{i}. {c.capitalize()}")
    choice = input("Enter option [1-5]: ")
    color_keys = ["red", "green", "yellow", "blue", "cyan"]
    return colors[color_keys[int(choice) - 1]]

# Menu system
def menu(username_color, username):
    while True:
        print(f"\n{username_color}Hello, {username}!" + colors["reset"])
        print(colors["cyan"] + "\nMain Menu:\n" + colors["reset"])
        print("1. Install Tools")
        print("2. About Developer")
        print("3. System Info")
        print("4. Exit\n")

        choice = input("Select an option: ")

        if choice == "1":
            install_tools()
        elif choice == "2":
            about_dev()
        elif choice == "3":
            system_info()
        elif choice == "4":
            os.system("cowsay 'Goodbye!' | lolcat")
            break
        else:
            print(colors["red"] + "Invalid option!" + colors["reset"])

# Tool installer
def install_tools():
    tools = ["git", "python", "python2", "curl", "wget", "figlet", "toilet", "cowsay", "nano", "sl", "lolcat"]
    for tool in tools:
        print(colors["blue"] + f"[*] Installing {tool}..." + colors["reset"])
        os.system(f"pkg install {tool} -y > /dev/null")
        print(colors["green"] + f"[✓] {tool} installed!" + colors["reset"])
        time.sleep(0.3)

# Developer info
def about_dev():
    os.system("clear")
    print(colors["cyan"] + "\n--- Developer Info ---" + colors["reset"])
    print(colors["white"] + "Name: Safwan")
    print("GitHub: github.com/Safwan146")
    print("Telegram: t.me/yourchannel")
    print("Facebook: fb.com/yourprofile")
    print(colors["cyan"] + "------------------------" + colors["reset"])
    input("\nPress Enter to return...")

# System info
def system_info():
    os.system("clear")
    print(colors["yellow"] + "\n--- System Info ---\n" + colors["reset"])
    os.system("uname -a")
    os.system("df -h")
    input("\nPress Enter to return...")

# Main
def main():
    os.system("termux-setup-storage")
    show_banner()
    username = input(colors["white"] + "Enter your name: ")
    user_color = choose_color()
    menu(user_color, username)

if __name__ == "__main__":
    main()