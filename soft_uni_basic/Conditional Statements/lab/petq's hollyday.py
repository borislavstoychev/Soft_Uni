# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
holiday_price = float(input())
num_puzzles = int(input())
num_barbie = int(input())
num_tedybear = int(input())
num_minions = int(input())
num_trucks = int(input())
total_price = num_puzzles * 2.60 + num_barbie * 3 + num_tedybear * 4.10 + num_minions * 8.20 + num_trucks * 2
total_toys = num_puzzles + num_barbie + num_tedybear + num_minions + num_trucks
if total_toys >= 50:
    discount = total_price * 0.25
    price = total_price - discount
else:
    price = total_price
rent = price * 0.10
win = price - rent
if win >= holiday_price:
    print(f"Yes!{win - holiday_price: .2f} lv left.")
else:
    print(f'Not enough money!{holiday_price - win: .2f} lv needed.')


