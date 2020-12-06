budget = float(input())
destination = input()
season = input()
days = int(input())

if season == 'Winter':
    if destination == 'Dubai':
        price = 45000 * days
        price *= 0.7
    elif destination == 'Sofia':
        price = 17000 * days
        price += price * 0.25
    elif destination == 'London':
        price = 24000 * days

elif season == 'Summer':
    if destination == 'Dubai':
        price = 40000 * days
        price *= 0.7
    elif destination == 'Sofia':
        price = 12500 * days
        price += price * 0.25
    elif destination == 'London':
        price = 20250 * days
if budget >= price:
    print(f'The budget for the movie is enough! We have {budget - price:.2f} leva left!')
if price > budget:
    print(f'The director needs {price - budget:.2f} leva more!')