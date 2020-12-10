age = int(input())
price_of_laundry = float(input())
toy_price = int(input())
money = 0
toy = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        money = money + (i * 5)
        money = money - 1
    else:
        toy = toy + 1
money_toy = toy * toy_price
total_money = money + money_toy
if total_money >= price_of_laundry:
    print(f'Yes! {total_money - price_of_laundry:.2f}')
else:
    print(f'No! {price_of_laundry - total_money:.2f}')
