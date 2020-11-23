command = input()
courses = {}
while not command == "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course] += [student]
    command = input()

for k, v in dict(sorted(courses.items(), key=lambda x: -len(x[1]))).items():
    print(f"{k}: {len(v)}")
    for i in sorted(v):
        print(f"-- {i}")
