name = input()
num_of_seasons = int(input())
num_of_series = int(input())
time = float(input())

time += time * 0.20
time_seasons = num_of_seasons * 10
total = num_of_seasons * time * num_of_series + time_seasons
print(f'Total time needed to watch the {name} series is {round(total)} minutes.')
