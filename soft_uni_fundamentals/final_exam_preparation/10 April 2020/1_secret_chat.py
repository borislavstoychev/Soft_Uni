concealed_message = input()
commands = input()
while not commands == "Reveal":
    command = commands.split(":|:")[0]
    if command == "InsertSpace":
        index = commands.split(":|:")[1]
        index = int(index)
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command == "Reverse":
        substring = commands.split(":|:")[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message += substring
            print(concealed_message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring, replacement = commands.split(":|:")[1:]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)
    commands = input()
print(f"You have a new text message: {concealed_message}")