n1 = int(input())
n2 = int(input())
n5 = int(input())
sum = int(input())
for i in range(n1 + 1):
    for j in range(n2 + 1):
        for k in range(n5 + 1):
            if (i * 1) + (j * 2) + (k * 5) == sum:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sum} lv.')