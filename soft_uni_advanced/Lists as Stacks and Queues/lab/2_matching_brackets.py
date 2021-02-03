line = input()
start = []
for index in range(len(line)):
    if line[index] == "(":
        start.append(index)
    elif line[index] == ")":
        print(line[start.pop():index + 1])



