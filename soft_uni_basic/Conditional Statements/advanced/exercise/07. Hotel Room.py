month = input()
nights = int(input())

price_per_studio = 0
price_per_apartment = 0

if month == 'May' or month == 'October':
    price_per_studio = 50
    price_per_apartment = 65
    if nights > 7 and nights <= 14:
        price_per_studio *= 0.95
    elif nights > 14:
        price_per_studio *= 0.7

elif month == 'June' or month == 'September':
    price_per_studio = 75.20
    price_per_apartment = 68.70
    if nights > 14:
        price_per_studio *= 0.8
elif month == 'July' or month == 'August':
    price_per_studio = 76
    price_per_apartment = 77
if nights > 14:
    price_per_apartment *= 0.9
print(f'Apartment:{nights * price_per_apartment: .2f} lv.')
print(f'Studio:{nights * price_per_studio: .2f} lv.')
