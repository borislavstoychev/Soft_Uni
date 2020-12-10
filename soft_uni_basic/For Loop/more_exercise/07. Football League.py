stadium_capacity = int(input())
num_of_fans = int(input())
kind_of_sectors = 0
s1, s2, s3, s4 = (0, 0, 0, 0)
for i in range(1, num_of_fans + 1):
    sector = input()
    if sector == 'A':
        kind_of_sectors += 1
        s1 += 1
    elif sector == 'B':
        kind_of_sectors += 1
        s2 += 1
    elif sector == 'V':
        kind_of_sectors += 1
        s3 += 1
    elif sector == 'G':
        kind_of_sectors += 1
        s4 += 1
print(f'{s1 / num_of_fans * 100:.2f}%')
print(f'{s2 / num_of_fans * 100:.2f}%')
print(f'{s3 / num_of_fans * 100:.2f}%')
print(f'{s4 / num_of_fans * 100:.2f}%')
print(f'{num_of_fans / stadium_capacity * 100:.2f}%')

