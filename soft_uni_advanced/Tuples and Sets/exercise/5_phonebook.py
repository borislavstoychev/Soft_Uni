phone_book = {}
line = input()
while not line.isdigit():
    name, phone = line.split("-")
    phone_book[name] = phone
    line = input()
for n in range(int(line)):
    names = input()
    if names in phone_book:
        print(f"{names} -> {phone_book[names]}")
    else:
        print(f"Contact {names} does not exist.")