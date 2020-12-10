change = float(input())

c = 0
change_coins = change * 100

while True:
    c += 1

    if change_coins >= 200:
        change_coins -= 200
    elif 100 <= change_coins:
        change_coins -= 100
    elif 50 <= change_coins:
        change_coins -= 50
    elif 20 <= change_coins:
        change_coins -= 20
    elif 10 <= change_coins:
        change_coins -= 10
    elif 5 <= change_coins:
        change_coins -= 5
    elif 2 <= change_coins:
        change_coins -= 2
    elif 1 <= change_coins:
        change_coins -= 1
    if change_coins < 1:
        break
print(c)