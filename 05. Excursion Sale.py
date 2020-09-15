sea = int(input())
mountain = int(input())
sea_price = 680
mountain_price = 499
price = 0
line = input()
while line != 'Stop':
    holiday = line
    if holiday == 'sea':
        if sea <= 0:
            price = price
        else:
            price += sea_price
            sea -= 1

    elif holiday == 'mountain':
        if mountain <= 0:
            price = price
        else:
            price += mountain_price
            mountain -= 1

    if sea == 0 and mountain == 0:
        print(f' Good job! Everything is sold.')
        break
    line = input()

print(f'Profit: {price} leva.')