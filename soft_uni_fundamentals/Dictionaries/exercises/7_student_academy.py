student_grades = {}

for _ in range(int(input())):
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = [grade]
    else:
        student_grades[name] += [grade]
for (key, value) in dict(sorted(student_grades.items(), key=lambda el: sum(el[1])/len(el[1]), reverse=True)).items():
    if sum(value) / len(value) >= 4.50:
        print(f"{key} -> {sum(value) / len(value):.2f}")
