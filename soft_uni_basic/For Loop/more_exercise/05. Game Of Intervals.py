n = int(input())
points = 0
p1, p2, p3, p4, p5, p6 = (0, 0, 0, 0, 0, 0)

for i in range(1, n + 1):
    new_num = int(input())
    if 0 <= new_num <= 9:
        points += 0.2 * new_num
        p1 += 1
    elif 10 <= new_num <= 19:
        points += 0.3 * new_num
        p2 += 1
    elif 20 <= new_num <= 29:
        points += 0.4 * new_num
        p3 += 1
    elif 30 <= new_num <= 39:
        points += 50
        p4 += 1
    elif 40 <= new_num <= 50:
        points += 100
        p5 += 1

    else:
        points /= 2
        p6 += 1

print(f'{points:.2f}')
print(f'From 0 to 9: {p1 / n * 100:.2f}%')
print(f'From 10 to 19: {p2 / n * 100:.2f}%')
print(f'From 20 to 29: {p3 / n * 100:.2f}%')
print(f'From 30 to 39: {p4 / n * 100:.2f}%')
print(f'From 40 to 50: {p5 / n * 100:.2f}%')
print(f'Invalid numbers: {p6 / n * 100:.2f}%')