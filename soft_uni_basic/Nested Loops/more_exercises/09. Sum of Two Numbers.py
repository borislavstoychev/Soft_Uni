n1 = int(input())
n2 = int(input())
magic_num = int(input())
count = 0
combination = False
for i in range(n1, n2 + 1):
    for j in range(n1, n2 + 1):
        count += 1
        if i + j == magic_num:
            combination = True
            print(f'Combination N:{count} ({i} + {j} = {magic_num})')
    if combination:
        break
if not combination:
    print(f'{count} combinations - neither equals {magic_num}')