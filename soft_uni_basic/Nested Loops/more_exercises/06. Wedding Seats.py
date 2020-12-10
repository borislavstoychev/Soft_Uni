end_of_sectors = input()
rows = int(input())
sits1 = int(input())

sits2 = sits1 + 2
r = 0
for a in range(65, ord(end_of_sectors) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 0:
            sits = sits2
        else:
            sits = sits1
        for s in range(97, sits + 97):
            r += 1
            print(f"{chr(a)}{row}{chr(s)}")
    rows += 1

print(r)


