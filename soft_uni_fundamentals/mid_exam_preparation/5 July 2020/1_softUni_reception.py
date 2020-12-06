employ_1 = int(input())
employ_2 = int(input())
employ_3 = int(input())
students = int(input())
total_per_hour = employ_1 + employ_2 + employ_3
hours = 0
while students > 0:
    hours += 1
    students -= total_per_hour
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")