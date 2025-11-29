# Python File & Folder Manager (CLI Project)

This is a command-line based **File & Folder Manager** written in Python.  
All operations are safely restricted to your project directory.

You will run the entire project using:

```bash
python main.py
```

---

## 📌 Features

### ✅ Folder Operations
- Create folder  
- List all files & folders  
- Rename folder  
- Delete folder (with safety check)

### ✅ File Operations
- Create file  
- Read file  
- Rename, append, or overwrite content  
- Delete file  

### 🔒 Safety Protection
To avoid accidental damage, the program restricts:
- Creating files/folders  
- Renaming  
- Deleting  
**Only inside the project directory** using the `is_inside_project()` checker.

---

## 📂 Project Structure

```
project-folder/
│
├── main.py        # Application code
└── README.md      # Documentation
```

---

## ▶️ How to Run the Program

1. Put your Python script in **main.py**
2. Open terminal in project folder
3. Run:

```bash
python main.py
```

4. You will see the menu:

```
1. Create folder
2. Read files/folders
3. Update folder
4. Delete folder
5. Create file
6. Read file
7. Update file
8. Delete file
0: Exit
```

---

## 📌 Menu Details

### 1️⃣ Create Folder
Creates a folder in the current project.

### 2️⃣ Read Files/Folders  
Shows all directories & files using:

```
Path().rglob("*")
```

### 3️⃣ Update Folder
Renames a selected folder.

### 4️⃣ Delete Folder  
Deletes a folder using:

```
rmdir /s /q "folder_name"
```

### 5️⃣ Create File  
Creates a file & writes content.

### 6️⃣ Read File  
Displays file content.

### 7️⃣ Update File  
Options:
- Rename  
- Append  
- Overwrite  

### 8️⃣ Delete File  
Deletes file inside the project folder.

---

## 🧾 Full Source Code (inside `main.py`)

```
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


# ------------------
# File Functions
# ------------------

def create_file():
    try:
        read_file_folder()
        name = input("Enter file name: ")
        p = Path(name).resolve()

        if not is_inside_project(p):
            print("You cannot create files outside project!")
            return

        if p.exists():
            print("File already exists")
            return

        with open(p, "w") as fs:
            data = input("Write what you want in this file: ")
            fs.write(data)

        print("File created successfully")
    except Exception as err:
        print(f"Error: {err}") 


def read_file():
    try:
        read_file_folder()
        name = input("Enter file name: ")
        p = Path(name).resolve()

        if not is_inside_project(p):
            print("Cannot read files outside project")
            return

        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                print("File content:")
                print(fs.read())
        else:
            print("File not found")

    except Exception as err:
        print(f"Error: {err}")


def update_file():
    try:
        read_file_folder()
        name = input("Enter file name: ")
        p = Path(name).resolve()

        if not is_inside_project(p):
            print("Cannot update file outside project")
            return

        if p.exists() and p.is_file():
            print("1. Rename file")
            print("2. Append content")
            print("3. Overwrite content")

            choice = int(input("Enter choice: "))

            if choice == 1:
                new_name = input("Enter new name with extension: ")
                new_p = Path(new_name)

                if new_p.exists():
                    print("File already exists with this name")
                else:
                    p.rename(new_p)
                    print("File renamed")

            elif choice == 2:
                with open(p, "a") as fs:
                    data = input("Enter text to append: ")
                    fs.write(" " + data)
                print("Data appended")

            elif choice == 3:
                with open(p, "w") as fs:
                    data = input("Enter new content: ")
                    fs.write(data)
                print("File overwritten")

            else:
                print("Invalid choice")

        else:
            print("File not found")

    except Exception as err:
        print(f"Error: {err}")


def delete_file():
    try:
        read_file_folder()
        name = input("Enter file name: ")
        p = Path(name).resolve()

        if not is_inside_project(p):
            print("Cannot delete files outside project")
            return

        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted")

        else:
            print("File not found")

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
print("5. Create file")
print("6. Read file")
print("7. Update file")
print("8. Delete file")
print("0: Exit")

try:
    choice = int(input("Enter your choice: "))
except:
    print("Invalid input! Please enter a number.")

while True:
    if choice == 1:
        create_folder()
    elif choice == 2:
        read_file_folder()
    elif choice == 3:
        update_folder()
    elif choice == 4:
        delete_folder()
    elif choice == 5:
        create_file()
    elif choice == 6:
        read_file()
    elif choice == 7:
        update_file()
    elif choice == 8:
        delete_file()
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
```

---
