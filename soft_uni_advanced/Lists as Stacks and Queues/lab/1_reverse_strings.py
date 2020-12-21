line = list(input())
reversed_line = []
while line:
    reversed_line.append(line.pop())

print(*reversed_line, sep="")