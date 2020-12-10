hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_exam_minutes = hour_exam * 60 + minute_exam
total_arrival_minutes = arrival_hour * 60 + arrival_minute

if total_exam_minutes - 30 <= total_arrival_minutes <= total_exam_minutes:
    print('On time')
    if total_exam_minutes != total_arrival_minutes:
        diff = total_exam_minutes - total_arrival_minutes
        print(f'{diff} minutes before the start')
elif total_arrival_minutes < total_exam_minutes - 30:
    print('Early')
    diff = total_exam_minutes - total_arrival_minutes
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        diff_hour = diff // 60
        diff_minutes = diff % 60
        if diff_minutes < 10:
            print(f'{diff_hour}:0{diff_minutes} hours before the start')
        else:
            print(f'{diff_hour}:{diff_minutes} hours before the start')
else:
    print('Late')
    diff = total_arrival_minutes - total_exam_minutes
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        diff_hour = diff // 60
        diff_minutes = diff % 60
        if diff_minutes < 10:
            print(f'{diff_hour}:0{diff_minutes} hours after the start')
        else:
            print(f'{diff_hour}:{diff_minutes} hours after the start')

