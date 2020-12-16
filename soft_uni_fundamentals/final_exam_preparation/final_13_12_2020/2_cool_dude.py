import re

pattern = r"(\*|@)(?P<name>[A-Z][a-z]{2,})(\*|@):\s\[(?P<group1>[a-zA-Z]+)\]\|\[(?P<group2>[a-zA-Z]+)\]\|\[(?P<group3>[a-zA-Z]+)\]"
n = int(input())

for _ in range(n):
    data = input()
    if re.finditer(pattern, data):
        result = ""
        tag_name = ""
        for match in re.finditer(pattern, data):
            result = match.group("group1") + match.group("group2") + match.group("group3")
            tag_name = match.group("name")
        letters = []
        for letter in result:
            num = ord(letter)
            letters.append(num)
        print(f"{tag_name}: ", end="")
        print(*letters, sep=" ")
    else:
        print("Valid message not found!")
