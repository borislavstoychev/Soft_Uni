secret_massage = input().split()
for el in secret_massage:
    new_character = []
    new_digit = []
    for character in el:
        if character.isalpha():
            new_character.append(character)
        else:
            decipher = int(character)
            new_digit.append(decipher)
    res = chr(int("".join(map(str, new_digit))))
    new_character[0], new_character[-1] = new_character[-1], new_character[0]
    characters = "".join(new_character)

    print(res + characters, end=' ')
