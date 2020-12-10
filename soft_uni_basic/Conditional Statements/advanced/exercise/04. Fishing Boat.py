budget = int(input())
season = input()
num_of_fisherman = int(input())

price_of_ship = 0

if season == 'Spring':
    price_of_ship = 3000
elif season == 'Summer' or season == 'Autumn':
    price_of_ship = 4200
elif season == 'Winter':
    price_of_ship = 2600
if num_of_fisherman % 2 == 0 and season != 'Autumn':
    price_of_ship *= 0.95
if num_of_fisherman <= 6:
    price_of_ship *= 0.9
elif 7 <= num_of_fisherman <= 11:
    price_of_ship *= 0.85
elif num_of_fisherman >= 12:
    price_of_ship *= 0.75
if budget >= price_of_ship:
    print(f'Yes! You have{budget - price_of_ship: .2f} leva left.')
else:
    print(f'Not enough money! You need{price_of_ship - budget: .2f} leva.')

