list_of_string = input().split()
repeated_string = ""
for l in list_of_string:
    repeated_string += l * len(l)

print(repeated_string)