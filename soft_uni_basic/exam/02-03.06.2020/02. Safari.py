budget = float(input())
gasoline = float(input())
day = input()

gasoline_price = gasoline * 2.10
price = gasoline_price + 100
if day == 'Saturday':
    price *= 0.90
elif day == 'Sunday':
    price *= 0.80

if budget >= price:
    print(f'Safari time! Money left: {budget - price:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {price - budget:.2f} lv.')