from math import ceil
count_of_the_students = int(input())
count_of_the_lectures = int(input())
the_initial_bonus = int(input())
max_bonus = 0
lecture = 0
for student in range(count_of_the_students):
    attendances_of_each_student = int(input())
    total_bonus = attendances_of_each_student / count_of_the_lectures * (5 + the_initial_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        lecture = attendances_of_each_student


print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {lecture} lectures.")

