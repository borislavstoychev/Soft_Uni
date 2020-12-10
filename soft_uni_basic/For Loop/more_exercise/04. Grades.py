num_student = int(input())
excellent, better, good, fail = (0, 0, 0, 0)
excellent_student, better_student, good_student, fail_student = (0, 0, 0, 0)
avr = 0

for i in range(1, num_student + 1):
    rating = float(input())
    if 5 <= rating <= 6:
        excellent += rating
        excellent_student += 1

    elif 4 <= rating <= 4.99:
        better += rating
        better_student += 1

    elif 3 <= rating <= 3.99:
        good += rating
        good_student += 1

    else:
        fail += rating
        fail_student += 1


avr = (excellent + better + good + fail) / num_student

print(f'Top students: {((excellent_student / num_student) * 100):.2f}%')
print(f'Between 4.00 and 4.99: {((better_student / num_student) * 100):.2f}%')
print(f'Between 3.00 and 3.99: {((good_student / num_student) * 100):.2f}%')
print(f'Fail: {((fail_student / num_student) * 100):.2f}%')
print(f'Average: {avr:.2f}')