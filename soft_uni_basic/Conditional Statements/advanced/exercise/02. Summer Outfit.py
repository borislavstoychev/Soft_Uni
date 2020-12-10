degrees = int(input())
time = input()
#if time == 'Morning' or time == 'Afternoon' or
outfit = ''
shoes = ''
if time == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = Shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = Shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time == 'Evening':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = Shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
else:
    print('Error')
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

