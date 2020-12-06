first_employ = int(input())
second_employ = int(input())
third_employ = int(input())
people_count = int(input())
hours = 0
for people in range(0, people_count, first_employ + second_employ + third_employ):
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f'Time needed: {hours}h.')
