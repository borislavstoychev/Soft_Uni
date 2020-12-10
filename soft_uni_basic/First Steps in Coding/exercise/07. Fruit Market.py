berry_price = float(input())
bananas_in_kg = float(input())
orange_in_kg = float(input())
raspberries_in_kg = float(input())
berry_in_kg = float(input())
raspberries_price = berry_price * 1/2
orange_price = raspberries_price - (raspberries_price * 40/100)
bananas_price = raspberries_price - (raspberries_price * 80/100)
total_price = berry_price * berry_in_kg + bananas_in_kg * bananas_price + raspberries_in_kg * raspberries_price + orange_in_kg * orange_price
print(total_price)

