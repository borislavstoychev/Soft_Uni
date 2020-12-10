n1 = int(input())
n2 = int(input())
total_price = 0
for i in range(1, n1 + 1):
    price = 0
    for j in range(1, n2 +1):
        if i % 2 == 0 and j % 2 != 0:
            price += 2.5
            continue
        if i % 2 != 0 and j % 2 == 0:
            price += 1.25
            continue
        else:
            price += 1
    else:
        print(f'Day: {i} - {price:.2f} leva')
    total_price += price
print(f'Total: {total_price:.2f} leva')
