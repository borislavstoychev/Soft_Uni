n = int(input())
p1, p2, p3, p4, p5 = (0, 0, 0, 0, 0)

for i in range(1, n+1):
    num = int(input())
    if num < 200:
        p1 += 1
    if 200 <= num <= 399:
        p2 += 1
    if 400 <= num <= 599:
        p3 += 1
    if 600 <= num <= 799:
        p4 += 1
    if num >= 800:
        p5 += 1
print(f'{p1 / n * 100:.2f}%')
print(f'{p2 / n * 100:.2f}%')
print(f'{p3 / n * 100:.2f}%')
print(f'{p4 / n * 100:.2f}%')
print(f'{p5 / n * 100:.2f}%')