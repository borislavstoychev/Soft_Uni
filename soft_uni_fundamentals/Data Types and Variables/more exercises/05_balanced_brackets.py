
number_of_lines = int(input())
left = 0
right = 0
opening = 0
for i in range(number_of_lines):
    string = input()
    if string == '(':
        left += 1
        opening += 1
    elif string == ')':
        right += 1
        opening = 0
    if opening == 2:
        break
if left == right:
    print('BALANCED')
else:
    print('UNBALANCED')