def password_validator(line):
    is_digit_and_letter = True
    if not (6 <= len(line) <= 10):
        is_digit_and_letter = False
        print("Password must be between 6 and 10 characters")
    count_digit = 0
    for element in line:
        if not element.isdigit():
            if not element.isalpha():
                is_digit_and_letter = False
                print("Password must consist only of letters and digits")
                break
        if element.isdigit():
            count_digit += 1
    if count_digit < 2:
        is_digit_and_letter = False
        print("Password must have at least 2 digits")
    if is_digit_and_letter:
        print("Password is valid")


password = input()

password_validator(password)

