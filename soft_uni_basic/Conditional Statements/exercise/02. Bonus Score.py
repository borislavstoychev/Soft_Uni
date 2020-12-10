num = int(input())
bonus = 0
if num <= 100:
    bonus = 5
    if num % 2 == 0:
        bonus = bonus + 1
    elif num % 10 == 5:
        bonus = bonus + 2
elif num > 100 and num <= 1000:
    bonus = (num * 0.2)
    if num % 2 == 0:
        bonus = bonus + 1
    elif num % 10 == 5:
        bonus = bonus + 2
elif num > 1000:
    bonus = (num * 0.1)
    if num % 2 == 0:
        bonus = bonus + 1
    elif num % 10 == 5:
        bonus = bonus + 2
print(bonus)
print(bonus + num)