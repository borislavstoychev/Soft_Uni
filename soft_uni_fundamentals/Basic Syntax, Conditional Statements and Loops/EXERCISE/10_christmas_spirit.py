quantity = int(input())
days = int(input())
sum = 0
spirit = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0:
        spirit -= 20
        sum += 5 + 3 + 15
        if day == days:
            spirit -= 30
    if day % 5 == 0:
        sum += quantity * 15
        spirit += 17
    if day % 15 == 0:
        spirit += 30
    if day % 3 == 0:
        sum += (quantity * 5) + (quantity * 3)
        spirit += 13
    if day % 2 == 0:
        sum += quantity * 2
        spirit += 5
print(f'Total cost: {sum}')
print(f'Total spirit: {spirit}')
