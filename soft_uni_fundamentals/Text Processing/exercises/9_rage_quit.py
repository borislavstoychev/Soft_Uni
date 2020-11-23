print_line = ""
num = ""
elements = ""
line = input().upper()
for index in range(len(line) + 1):
    if index not in range(len(line)):
        print_line += (elements * int(num))
        break
    if line[index].isdigit():
        num += line[index]
    elif not num == "":
        print_line += (elements * int(num))
        num = ""
        elements = ""
        if not line[index].isdigit():
            elements += line[index]
    else:
        elements += line[index]

print(f"Unique symbols used: {len(set(print_line))}")
print(print_line)

