from math import floor
income = float(input())
avr_grade = float(input())
min_salary = float(input())

social_schularship = 0
garde_schularship = 0

if avr_grade >= 4.50 and income < min_salary:
    social_schularship = min_salary * 0.35
if avr_grade > 5.5:
    garde_schularship = avr_grade * 25
if social_schularship == 0 and garde_schularship == 0:
    print('You cannot get a scholarship!')
elif social_schularship != 0 and garde_schularship == 0:
    print(f'You get a Social scholarship {floor (social_schularship)} BGN')
elif social_schularship == 0 and garde_schularship != 0:
    print(f'You get a scholarship for excellent results {floor(garde_schularship)} BGN')
else:
    if social_schularship > garde_schularship:
        print(f'You get a Social scholarship {floor (social_schularship)} BGN')
    else:
        print(f'You get a scholarship for excellent results {floor(garde_schularship)} BGN')
