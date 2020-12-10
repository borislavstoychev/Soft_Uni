budget = float (input())
seasons = input()

destination = ''
money_spent = 0
kind_of_holidays = ''
if budget <= 100:
    destination = 'Bulgaria'
    if seasons == 'summer':
        kind_of_holidays = 'Camp'
        money_spent = budget * 0.3
    elif seasons == 'winter':
        kind_of_holidays = 'Hotel'
        money_spent = budget * 0.7
elif  budget <= 1000:
    destination = 'Balkans'
    if seasons == 'summer':
        kind_of_holidays = 'Camp'
        money_spent = budget * 0.4
    elif seasons == 'winter':
        kind_of_holidays = 'Hotel'
        money_spent = budget * 0.8
else:
    destination = 'Europe'
    kind_of_holidays = 'Hotel'
    money_spent = budget * 0.9
print(f'Somewhere in {destination}')
print(f'{kind_of_holidays} -{money_spent: .2f}')
