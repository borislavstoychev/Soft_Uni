user_name = input()
commands = input()
while not commands == "Sign up":
    command = commands.split()[0]
    if command == "Case":
        lower_upper = commands.split()[1]
        if lower_upper == "lower":
            user_name = user_name.lower()
            print(user_name)
        else:
            user_name = user_name.upper()
            print(user_name)
    elif command == "Reverse":
        start_index, end_index = commands.split()[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index >= 0 and end_index < len(user_name):
            new_user = user_name[start_index:end_index + 1]
            new_user = new_user[::-1]
            print(new_user)
    elif command == "Cut":
        substring = commands.split()[1]
        if substring in user_name:
            user_name = user_name.replace(substring, "")
            print(user_name)
        else:
            print(f"The word {user_name} doesn't contain {substring}.")
    elif command == "Replace":
        characters = commands.split()[1]
        if characters in user_name:
            user_name = user_name.replace(characters, "*")
            print(user_name)
    elif command == "Check":
        character = commands.split()[1]
        if character in user_name:
            print("Valid")
        else:
            print(f"Your username must contain {character}.")

    commands = input()