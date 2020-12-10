from math import floor
year = input()
playday = int(input())
holiday = int(input())

tota_volleybal_holiday = 48
volleybal_holiday_sofia = (tota_volleybal_holiday - holiday) * 0.75
volleybal_playday = playday * 2/3
total_game = volleybal_holiday_sofia + holiday + volleybal_playday

if year == 'leap':
    total_game += total_game * 0.15
    print(floor(total_game))
else:
    print(floor(total_game))
