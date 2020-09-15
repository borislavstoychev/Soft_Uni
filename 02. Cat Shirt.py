sleeve_size = float(input())
face_part = float(input())
cloth = input()
tie = input()
shirt_price = (2 * sleeve_size) + (2 * face_part)
shirt_price += shirt_price * 0.1
shirt_price /= 100
if cloth == 'Linen':
    shirt_price *= 15
elif cloth == 'Cotton':
    shirt_price *= 12
elif cloth == 'Denim':
    shirt_price *= 20
elif cloth == 'Twill':
    shirt_price *= 16
elif cloth == 'Flannel':
    shirt_price *= 11
shirt_price += 10
if tie == 'Yes':
    shirt_price += (shirt_price * 0.2)
    print(f'The price of the shirt is: {shirt_price:.2f}lv.')
else:
    print(f'The price of the shirt is: {shirt_price:.2f}lv.')