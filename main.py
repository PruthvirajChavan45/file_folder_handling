from pathlib import Path
import os

# ------------------
# SAFETY: Delete only INSIDE project folder
# ------------------

PROJECT_ROOT = Path.cwd().resolve()   # Current project folder

def is_inside_project(path: Path):
    """Check if the path is inside project directory."""
    try:
        return str(path.resolve()).startswith(str(PROJECT_ROOT))
    except Exception:
        return False


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


def update_folder():
    try:
        read_file_folder()
        old_name = input("Which folder do you want to rename? ")
        p = Path(old_name).resolve()

        if not is_inside_project(p):
            print("You cannot rename folder outside this project.")
            return

        if p.exists() and p.is_dir():
            new_name = input("Enter new folder name: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Folder renamed successfully")
        else:
            print("Folder not found")

    except Exception as err:
        print(f"Error: {err}")


def delete_folder():
    try:
        read_file_folder()
        name = input("Which folder do you want to delete? ")
        p = Path(name).resolve()

        # SAFETY CHECK
        if not is_inside_project(p):
            print("You cannot delete folders outside this project!")
            return

        if not p.exists():
            print("Folder does not exist")
            return

        if not p.is_dir():
            print("This is not a folder")
            return

        print(f"Deleting folder: {p}")
        command = f'rmdir /s /q "{p}"'    # force delete inside project
        os.system(command)

        print("Folder deleted successfully")

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
elif choice == 2:
        read_file_folder()
elif choice == 3:
        update_folder()
elif choice == 4:
     delete_folder()