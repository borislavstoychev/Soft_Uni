a = int(input())
b = int(input())
a1 = int(input()) + a
b1 = int(input()) + b
n = 0
n1 = 0

for i in range(a, a1 + 1):
    n = 0
    if i > 1:
        for num in range(2, i):
            if (i % num) == 0:
                break
        else:
            n = i
    if n == 0:
        continue

    for j in range(b, b1 + 1):
        if j > 1:
            for k in range(2, j):
                if (j % k) == 0:
                    break
            else:
                n1 = j
                print(f'{n}{n1}')
