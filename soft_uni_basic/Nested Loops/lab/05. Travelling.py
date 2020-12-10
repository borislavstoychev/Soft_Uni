while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    curent_money = 0
    while curent_money < budget:
        money = float(input())
        curent_money += money
    print(f'Going to {destination}!')

