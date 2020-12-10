n = int(input())
l = int(input())

for k in range(1, n + 1):
    for j in range(1, n + 1):
        for a in range(97, 97 + l):
            for m in range(97, 97 + l):
                for i in range(1, n + 1):
                    if i > k and i > j:
                        print(f'{k}{j}{chr(a)}{chr(m)}{i}', end= ' ')