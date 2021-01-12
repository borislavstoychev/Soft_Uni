elements = set()
for el in range(int(input())):
    for e in input().split():
        elements.add(e)
print(*elements, sep="\n")