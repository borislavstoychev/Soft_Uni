import sys
number_of_snowballs = int(input())
max_snowball_snow = None
max_snowball_time = None
max_snowball_quality = None
max_score = -sys.maxsize
for i in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    score = (snowball_snow / snowball_time) ** snowball_quality
    if score > max_score:
        max_score = score
        max_snowball_quality = snowball_quality
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time

print(f'{max_snowball_snow} : {max_snowball_time} = {int(max_score)} ({max_snowball_quality})')