n1 = int(input())
n2 = int(input())
num1 = 0
num2 = 0
num3 = 0
num4 = 0
for a in range(n1, n2 + 1):
    for b in range(n1, n2 + 1):
        for c in range(n1, n2 + 1):
            for d in range(n1, n2 + 1):
                if a > d and (b + c) % 2 == 0:
                    num1 = a
                    num2 = b
                    num3 = c
                else:
                    continue
                if a % 2 == 0 and d % 2 != 0:
                    num1 = a
                    num4 = d

                elif a % 2 != 0 and d % 2 == 0:
                    num1 = a
                    num4 = d
                else:
                    continue

                print(f'{a}{b}{c}{d}', end=' ')

