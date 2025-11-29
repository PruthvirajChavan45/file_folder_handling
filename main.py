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