line = input()
for index in range(len(line)):
    if line[index] == ":":
        print(line[index:index + 2])