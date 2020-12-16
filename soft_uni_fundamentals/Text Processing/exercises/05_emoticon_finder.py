line = input()
for index in range(len(line) - 1):
    if line[index] == ":":
        print(line[index:index + 2])