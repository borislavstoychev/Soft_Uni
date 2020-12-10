n = int(input())
salary = int(input())
site = ''
for i in range(1, n+1):
    site = input()
    if site == 'Facebook':
        salary -= 150
    if site == 'Instagram':
        salary -= 100
    if site == 'Reddit':
        salary -= 50
    else:
        salary = salary
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')