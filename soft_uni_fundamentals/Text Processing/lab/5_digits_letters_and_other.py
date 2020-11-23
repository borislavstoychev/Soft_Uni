digits = ""
alpha = ""
other = ""
single_string = input()
for l in single_string:
    if l.isdigit():
        digits += l
    elif l.isalpha():
        alpha += l
    else:
        other += l

print(digits)
print(alpha)
print(other)
