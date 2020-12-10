time = int(input())
day = input()
if time < 10 or time > 18 or day == 'Sunday':
    print('closed')
elif time >= 10 or time <= 18 or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thuesday' or day == 'Friday' or day == 'Saturday':
    print('open')
else:
    print('Error')