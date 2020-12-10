kind_of_flowers = input()
num_of_flowers = int(input())
budget = int(input())

price_per_rose = 5
price_per_dahlias = 3.80
price_per_tulips = 2.80
price_per_narcissus = 3
price_per_gladiolus = 2.50

if kind_of_flowers == 'Roses':
    if num_of_flowers > 80:
        total_price = num_of_flowers * price_per_rose - (num_of_flowers * price_per_rose * 0.1)
    else:
        total_price = num_of_flowers * price_per_rose
elif kind_of_flowers == 'Dahlias':
    if num_of_flowers >90:
        total_price = num_of_flowers * price_per_dahlias - (num_of_flowers * price_per_dahlias * 0.15)
    else:
        total_price = num_of_flowers * price_per_dahlias
elif kind_of_flowers == 'Tulips':
    if num_of_flowers > 80:
        total_price = num_of_flowers * price_per_tulips -(num_of_flowers * price_per_tulips * 0.15)
    else:
        total_price = num_of_flowers * price_per_tulips
elif kind_of_flowers == 'Narcissus':
    if num_of_flowers < 120:
        total_price = num_of_flowers * price_per_narcissus + (num_of_flowers * price_per_narcissus * 0.15)
    else:
        total_price = num_of_flowers * price_per_narcissus
elif kind_of_flowers == 'Gladiolus':
    if num_of_flowers < 80:
        total_price = num_of_flowers * price_per_gladiolus + (num_of_flowers * price_per_gladiolus * 0.20)
    else:
        total_price = num_of_flowers * price_per_gladiolus
else:
    print('Error')
if budget >= total_price:
    print(f'Hey, you have a great garden with {num_of_flowers} {kind_of_flowers} and{budget - total_price: .2f} leva left.')
else:
    print(f'Not enough money, you need{total_price - budget: .2f} leva more.')