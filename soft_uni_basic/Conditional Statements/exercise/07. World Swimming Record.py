from math import floor
record = float(input())
distance_meters = float(input())
time_sec_m= float(input())
time_to_swim = distance_meters * time_sec_m
time_sec_m = (floor(distance_meters // 15) * 12.5)
calculate_time = (time_to_swim) + time_sec_m
if record > calculate_time:
    print(f'Yes, he succeeded! The new world record is{calculate_time: .2f} seconds.')
else:
    print(f'No, he failed! He was{calculate_time - record: .2f} seconds slower.')
