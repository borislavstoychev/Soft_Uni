money = float(input())
year = int(input())
spent_money = 0
years_old = 18

for i in range(1800, year + 1):
    if i % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + 50 * years_old

    years_old += 1

if spent_money <= money:
    print(f'Yes! He will live a carefree life and will have {money - spent_money:.2f} dollars left.')
else:
    print(f'He will need {spent_money - money:.2f} dollars to survive.')