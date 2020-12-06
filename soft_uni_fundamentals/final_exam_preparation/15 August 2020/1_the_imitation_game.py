line = input()

commands = input()
while not commands == "Decode":
    try:
        command, number_of_letters = commands.split("|")
        number_of_letters = int(number_of_letters)
        if command == "Move":
            line = line[number_of_letters:] + line[:number_of_letters]
    except ValueError:
        command, token1, token2 = commands.split("|")
        if command == "Insert":
            index = int(token1)
            value = token2
            line = line[:index] + value + line[index:]
        elif command == "ChangeAll":
            substring, replacement = token1, token2
            line = line.replace(substring, replacement)

    commands = input()
print(f"The decrypted message is: {line}")