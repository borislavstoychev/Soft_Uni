def characters_in_range(a, b):
    character_list = []
    for i in range(ord(a) + 1, ord(b)):
        character_list.append(chr(i))
    return character_list


A = input()
B = input()

print(' '.join(characters_in_range(A, B)))
