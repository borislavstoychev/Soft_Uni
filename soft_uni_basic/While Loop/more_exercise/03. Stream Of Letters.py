secret_letter1 = False
secret_letter2 = False
secret_letter3 = False
output = ''
current_word = ''
while True:
    if secret_letter1 and secret_letter2 and secret_letter3:
        output += current_word + ' '
        current_word = ''
        secret_letter1 = False
        secret_letter2 = False
        secret_letter3 = False

    letter_input = input()
    if letter_input == 'End':
        break

    ascii_char = ord(letter_input)
    if not(65 <= ascii_char <= 90 or 97 <= ascii_char <= 122):
        continue

    if letter_input == 'c' and not secret_letter1:
        secret_letter1 = True
        continue
    elif letter_input == 'o' and not secret_letter2:
        secret_letter2 = True
        continue
    elif letter_input == 'n' and not secret_letter3:
        secret_letter3 = True
        continue

    current_word += letter_input

print(output)
