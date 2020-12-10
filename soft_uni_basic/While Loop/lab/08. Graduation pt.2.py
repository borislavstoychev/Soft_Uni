name = input()
grades = 1
sum_of_grads = 0
excluded = 0

while grades <= 12:
    grade = float(input())
    if grade < 4:
        excluded += 1
        if excluded > 1:
            print(f'{name} has been excluded at {grades} grade')
            break
        continue
    sum_of_grads += grade
    grades += 1
if excluded != 2:
    print(f'{name} graduated. Average grade: {sum_of_grads / 12:.2f}')
