import os

# রঙের অপশন
colors = {
    "red": "\\e[1;31m",
    "green": "\\e[1;32m",
    "yellow": "\\e[1;33m",
    "blue": "\\e[1;34m",
    "magenta": "\\e[1;35m",
    "cyan": "\\e[1;36m"
}

def create_banner(name, color_code):
    banner_text = f"""
echo -e "{color_code}"
figlet -f slant "{name}"
echo -e "\\e[0m"
echo -e "\\e[1;37m       Developed by Safwan\\e[0m"
"""
    bashrc_path = os.path.expanduser("~/.bashrc")

    with open(bashrc_path, "a") as file:
        file.write("\n" + banner_text)

    print("\n[✓] Banner added successfully!")
    print("Open a new Termux session to see your banner.")

def install_dependencies():
    print("[*] Installing figlet...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install figlet -y")

def select_color():
    print("\nChoose a banner color:")
    for i, color in enumerate(colors.keys(), start=1):
        print(f"{i}. {color.title()}")
    choice = input("Enter choice number (e.g., 1): ")
    try:
        color_key = list(colors.keys())[int(choice)-1]
        return colors[color_key]
    except:
        print("Invalid choice. Defaulting to green.")
        return colors["green"]

def main():
    os.system("clear")
    print("=== Termux Banner Maker ===\n")
    name = input("Enter your name (or custom banner text): ")
    color = select_color()
    install_dependencies()
    create_banner(name, color)

if __name__ == "__main__":
    main()
