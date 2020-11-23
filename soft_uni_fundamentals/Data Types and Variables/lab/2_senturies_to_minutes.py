centuries = int(input())
one_year_in_days = 365.2422
one_day_in_hours = 24
one_hour_in_min = 60

years = centuries * 100
days = int(years * one_year_in_days)
hours = days * one_day_in_hours
minutes = hours * one_hour_in_min
print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')

