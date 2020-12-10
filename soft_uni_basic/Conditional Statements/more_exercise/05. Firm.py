from math import  floor

hour = int(input())
days_to_finish_the_projrct = int(input())
num_of_employ_overtime = int(input())

ten_precent = days_to_finish_the_projrct * 0.9
work_hour_projrct = ten_precent * 8
over_time = num_of_employ_overtime * (2 * days_to_finish_the_projrct)
finish_time = floor(work_hour_projrct + over_time)

if finish_time >= hour:
    print(f'Yes!{finish_time - hour} hours left.')
else:
    print(f'Not enough time!{hour - finish_time} hours needed.')