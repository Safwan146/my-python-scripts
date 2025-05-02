# read_notes.py

def read_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("তোমার নোটস:\n")
            print(content)
    except FileNotFoundError:
        print("notes.txt ফাইল খুঁজে পাওয়া যায়নি!")

if __name__ == "__main__":
    read_notes()