import math
time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second +time_third
minutes = total_time / 60
secconds = total_time % 60
minutes = math.floor(minutes)
if secconds < 10:
    print(f'{minutes}:0{secconds}')
else:
    print(f'{minutes}:{secconds}')