num_1 = int(input())
num_2 = int(input())
operator = input()
result = 0
even_or_odd = ''
if operator == '+':
    result = num_1 + num_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{num_1} {operator} {num_2} = {result} - {even_or_odd}')
elif operator == '-':
    result = num_1 - num_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{num_1} {operator} {num_2} = {result} - {even_or_odd}')
elif operator == '*':
    result = num_1 * num_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{num_1} {operator} {num_2} = {result} - {even_or_odd}')
if operator == '/':
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
    else:
        result = num_1 / num_2
        print(f'{num_1} / {num_2} ={result: .2f}')
if operator == '%':
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
    else:
        result = num_1 % num_2
        print(f'{num_1} % {num_2} = {result}')
