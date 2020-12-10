num_of_days = int(input())
money_win = 20
total_win = 0
total_lost = 0
total_money = 0
for i in range(num_of_days):
    line = input()
    win = 0
    lost = 0
    money = 0
    while line != 'Finish':
        sport = line
        result = input()
        if result == 'win':
            win += 1
            money += money_win
        if result == 'lose':
            lost += 1
        line = input()
    if win > lost:
        money += money * 0.1
    total_money += money
    total_win += win
    total_lost += lost
if total_win > total_lost:
    total_money = total_money + total_money * 0.2
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
