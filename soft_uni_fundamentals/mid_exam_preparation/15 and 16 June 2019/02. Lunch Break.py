from math import ceil
name = input()
time = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
rest_time = break_time * 0.25
left_time = (break_time - rest_time - lunch_time)
if time <= left_time:
    print(f'You have enough time to watch {name} and left with {ceil(left_time - time)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(abs(left_time - time))} more minutes.")
