items_with_their_prices = input().split("|")
budget = float(input())

bought_items = []
profit = 0

for items in items_with_their_prices:
    type_item, price = items.split("->")
    price = float(price)
    if type_item == "Clothes" and price > 50:
        continue
    elif type_item == "Shoes" and price > 35:
        continue
    elif type_item == "Accessories" and price > 20.50:
        continue
    if budget >= price:
        budget -= price
        current_profit = price * 0.40
        profit += current_profit
        bought_items.append(price + current_profit)

for el in bought_items:
    print(f"{el:.2f} ", end='')

budget += sum(bought_items)
print()
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
