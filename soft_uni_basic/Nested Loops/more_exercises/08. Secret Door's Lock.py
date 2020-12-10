n1 = int(input())
n2 = int(input())
n3 = int(input())

for i in range(1, n1 + 1):
    if i % 2 == 0:
        for j in range(1, n2 + 1):
            if j == 2 or j == 3 or j == 5 or j == 7:
                for k in range(1, + n3 + 1):
                    if k % 2 == 0:
                        print(f'{i} {j} {k}')