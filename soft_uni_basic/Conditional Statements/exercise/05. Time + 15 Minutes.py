hour = int(input())
minutes = int(input())
hour = hour + (minutes + 15)//60
if hour > 23:
    hour = 0
minutes = (minutes + 15) % 60
if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')

