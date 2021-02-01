import os


def creat(file):
    with open(file, "w") as file:
        return file.writelines("")


def add(file, message):
    with open(file, "a") as file:
        return file.write(message + "\n")


def replace(file, old, new):
    try:
        with open(file, "r+") as file:
            tex = "".join(file)
            new_tex = tex.replace(old, new)
            file.seek(0)
            return file.write(new_tex)
    except FileNotFoundError:
        print("An error occurred")


def delete(file):
    if os.path.exists(file):
        return os.remove(file)

    else:
        print("An error occurred")


commands = input()
while not commands == "End":
    command = commands.split("-")[0]
    if command == "Create":
        file = commands.split("-")[1]
        creat(file)
    elif command == "Add":
        file, message = commands.split("-")[1:]
        add(file, message)
    elif command == "Replace":
        file, old, new = commands.split("-")[1:]
        replace(file, old, new)
    elif command == "Delete":
        file = commands.split("-")[1]
        delete(file)
    commands = input()
