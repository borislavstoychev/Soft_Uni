kilometers = int(input())
day_night = input()

if kilometers < 20:
    if day_night == 'day':
        const_tax = 0.70
        day_tax = 0.79
        total_price = 0.70 + (kilometers * day_tax)
        print(f'{total_price:.2f}')
    else:
        night_tax = 0.90
        total_price = 0.70 + (kilometers * night_tax)
        print(f'{total_price:.2f}')
elif 20 <= kilometers < 100:
    total_price = kilometers * 0.09
    print(f'{total_price:.2f}')

elif kilometers >= 100:
    total_price = kilometers * 0.06
    print(f'{total_price:.2f}')
