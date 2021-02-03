import re

pattern = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<message>[a-zA-Z]{8,})\]"
n = int(input())
for _ in range(n):
    data = input()
    if re.match(pattern, data):
        command, message = data.split("!:[")
        command = command[1:]
        message = message[:-1]
        letters_list = []
        for letters in message:
            letter = ord(letters)
            letters_list.append(letter)
        print(f"{command}: ", end="")
        print(*letters_list, sep=" ")
    else:
        print("The message is invalid")
