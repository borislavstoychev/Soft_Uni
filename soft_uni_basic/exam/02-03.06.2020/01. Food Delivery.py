chicken = int(input())
fish = int(input())
vegetable = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.40
vegetable_price = vegetable * 8.15
total_price = chicken_price + fish_price + vegetable_price

desert_price = total_price * 0.20
total_price += desert_price + 2.50
print(f'Total: {total_price:.2f}')