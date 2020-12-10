n1 = int(input())
n2 = int(input())
n3 = int(input())

for i in range(2, n1 + 1, 2):
    for j in range(2, n2 + 1):
        for k in range(2, n3 + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f"{i} {j} {k}")