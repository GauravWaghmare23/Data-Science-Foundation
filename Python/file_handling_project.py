from pathlib import Path


def readFileAndFolderPath():
    path = Path('.')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i} : {item}")


def createFile():
    try:
        readFileAndFolderPath()
        choice = input("Enter the name of file you want to create: ")
        p = Path(choice)

        if p.exists():
            print("File already exists")
            return

        with open(p, 'w') as file:
            data = input(f"Enter the content for {p.name}: ")
            file.write(data)

        print("File created successfully")

    except Exception as e:
        print("Error:", e)


def readFile():
    try:
        readFileAndFolderPath()
        choice = input("Enter the file to read: ")
        p = Path(choice)

        if not (p.exists() and p.is_file()):
            print("File does not exist")
            return

        with open(p, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)

        print("File read successfully")

    except Exception as e:
        print("Error:", e)


def updateFile():
    try:
        readFileAndFolderPath()
        choice = input("Enter the file you want to update: ")
        p = Path(choice)

        if not (p.exists() and p.is_file()):
            print("File does not exist")
            return

        print("Press 1 for overwriting the file")
        print("Press 2 to append a new line")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input")
            return

        if option == 1:
            confirm = input("This will overwrite the file. Continue? (y/n): ")
            if confirm.lower() != 'y':
                print("Operation cancelled")
                return

            with open(p, 'w') as file:
                data = input("Enter new content: ")
                file.write(data)

            print("File overwritten successfully")

        elif option == 2:
            with open(p, 'a') as file:
                data = input("Enter content to append: ")
                file.write("\n" + data)

            print("Content appended successfully")

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)


def deleteFile():
    try:
        readFileAndFolderPath()
        choice = input("Enter the file you want to delete: ")
        p = Path(choice)

        if not (p.exists() and p.is_file()):
            print("File does not exist")
            return

        confirm = input("Are you sure you want to delete this file? (y/n): ")
        if confirm.lower() != 'y':
            print("Deletion cancelled")
            return

        p.unlink()
        print("File deleted successfully")

    except Exception as e:
        print("Error:", e)



while True:
    print("\n--- FILE MANAGER ---")
    print("1. Create File")
    print("2. Read File")
    print("3. Delete File")
    print("4. Update File")
    print("5. Exit")

    try:
        num = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if num == 1:
        createFile()
    elif num == 2:
        readFile()
    elif num == 3:
        deleteFile()
    elif num == 4:
        updateFile()
    elif num == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")