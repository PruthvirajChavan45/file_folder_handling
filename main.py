from pathlib import Path
import os

# ------------------
# Folder Functions
# ------------------

def create_folder():
    try:
        name = input("Please tell your folder name: ")
        p = Path(name)
        p.mkdir()
        print("Folder created successfully")
    except Exception as err:
        print(f"Error: {err}")


def read_file_folder():
    p = Path(".")          # Current folder
    items = list(p.rglob("*"))
    for i, v in enumerate(items): 
         print(f"{i + 1} : {v}")


# -------------
# MAIN MENU
# -------------

print("\nOptions:")
print("1. Create folder")
print("2. Read files/folders")
print("3. Update folder")
print("4. Delete folder")

try:
    choice = int(input("Enter your choice: "))
except:
    print("Invalid input! Please enter a number.")


if choice == 1:
        create_folder()

elif choice == 2:
        read_file_folder()