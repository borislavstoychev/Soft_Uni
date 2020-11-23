employee_happiness = list(map(int, input().split()))
happiness_factor = int(input())

employee = list(x * happiness_factor for x in employee_happiness)
filtered = list(filter(lambda x: x >= sum(employee)/len(employee), employee))

if len(filtered) <= len(employee) / 2:
    print(f"Score {len(filtered)}/{len(employee)}. Employees are not happy!")
else:
    print(f"Score: {len(filtered)}/{len(employee)}. Employees are happy!")
