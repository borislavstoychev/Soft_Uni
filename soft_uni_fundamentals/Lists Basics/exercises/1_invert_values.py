string = input()
new_string = string.split()
opposite_string = []
for num in range(len(new_string)):
    opposite = int(new_string[num]) * (-1)
    opposite_string.append(opposite)
print(opposite_string)
