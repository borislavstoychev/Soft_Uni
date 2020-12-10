n1 = int(input())
n2 = int(input())
n3 = int(input())
num1 = ''
num2 = ''
num3 = ''
for a in range(1, n1 + 1):
    if a % 2 == 0:
        num1 = a
    else:
        continue
    for b in range(1, n2 + 1):
        if b == 2 or b == 3 or b == 5 or b == 7:
            num2 = b
        else:
            continue
        for c in range(1, n3 + 1):
            if c % 2 == 0:
                num3 = c
            else:
                continue

            print(f'{num1} {num2} {num3}', end='')
            print()





