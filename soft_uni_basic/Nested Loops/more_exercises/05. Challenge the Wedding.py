male = int(input())
female = int(input())
num_of_tables = int(input())

for a in range(1, num_of_tables):
    for m in range(1, male + 1):
        if m > male:
            break
        for f in range(1, female + 1):

            if f > female:
                break
            elif a > num_of_tables:
                break
            a += 1
            print(f'({m} <-> {f})', end=' ')
    else:
        break
