budget = float(input())
num_of_statistics = float(input())
price_outfit = float(input())

decore_price = budget * 0.1
if num_of_statistics > 150:
    price_outfit -= price_outfit * 0.1
total_outfit_price = num_of_statistics * price_outfit
total_movie_price = decore_price + total_outfit_price

if total_movie_price > budget:
    print('Not enough money!')
    print(f'Wingard needs{total_movie_price - budget: .2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with{budget -total_movie_price: .2f} leva left.')
