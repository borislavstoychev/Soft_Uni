fruit = input()
day = input()
qty = float(input())
if day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    elif fruit != 'banana' or fruit != 'apple' or fruit != 'orange' or fruit!= 'grapefruit' or fruit != 'kiwi' or fruit != 'pineaple' or fruit != 'grapes':
        price = 0
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    elif fruit != 'banana' or fruit != 'apple' or fruit != 'orange' or fruit != 'grapefruit' or fruit != 'kiwi' or fruit != 'pineaple' or fruit != 'grapes':
        price = 0
else:
    price = 0
total_price = qty * price
if price == 0:
    print('error')
else:
    print(f'{total_price : .2f}')

