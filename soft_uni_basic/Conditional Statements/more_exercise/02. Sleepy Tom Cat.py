from math import floor
num_of_holiday = int(input())

limit_play_game = 30000
working_day = 365 - num_of_holiday

play_time_in_working_day = working_day * 63
play_time_in_holiday = num_of_holiday * 127
total_time = play_time_in_holiday + play_time_in_working_day

if total_time > limit_play_game:
    final_time = total_time - limit_play_game
    H = floor(final_time // 60)
    M = floor(final_time % 60)
    print('Tom will run away')
    print(f'{H} hours and {M} minutes more for play')
else:
    final_time = limit_play_game - total_time
    H = floor(final_time // 60)
    M = floor(final_time % 60)
    print('Tom sleeps well')
    print(f'{H} hours and {M} minutes less for play')