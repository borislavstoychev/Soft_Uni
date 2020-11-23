line = input()
new_str = ""
new_letter = ""
for letter in line:
    if not letter == new_letter:
        new_str += letter
    new_letter = letter
print(new_str)


