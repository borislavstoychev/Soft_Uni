days = int(input())
rooms = input()
rating = input()
if rooms == 'room for one person':
    price = 18
elif rooms == 'apartment':
    price = 25
    if days < 10:
        price = 25 - (25 * 0.3)
    elif days >= 10 and days <= 15:
        price = price - (price * 0.35)
    elif days > 15:
        price = price - (price * 0.5)
elif rooms == 'president apartment':
    price = 35
    if days < 10:
        price = 25 - (25 * 0.1)
    elif days >= 10 and days <= 15:
        price = price - (price * 0.15)
    elif days > 15:
        price = price - (price * 0.2)
else:
    price = 0
if rating == 'positive':
    amaunt = (days - 1) * price + ((days - 1) * price * 0.25)
    print(f'{amaunt:.2f}')
elif rating == 'negative':
    amaunt = (days - 1) * price - ((days -1) * price * 0.1)
    print(f'{amaunt: .2f}')
else:
    print('Error')