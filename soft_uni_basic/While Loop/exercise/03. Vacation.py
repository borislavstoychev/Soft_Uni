money_needed = float(input())
money_have = float(input())

count_spent_days =0
days = 0

while money_have < money_needed and count_spent_days < 5:
    text = input()
    money_save = float(input())

    if text == 'save':
        money_have += money_save
        count_spent_days = 0
    elif text == 'spend':
        money_have -= money_save
        if money_have < 0:
            money_have = 0
        count_spent_days += 1


    days += 1
if count_spent_days == 5:
    print("You can't save the money.")
    print(f'{days}')
if money_have >= money_needed:
    print(f'You saved the money for {days} days.')