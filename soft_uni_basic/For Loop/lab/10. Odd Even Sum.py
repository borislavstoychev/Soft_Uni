n = int(input())

eve_num = 0
odd_num = 0

for i in range(1,n+1):
    element = int(input())
    if i % 2 == 0:
        eve_num += element
    else:
        odd_num += element
if eve_num == odd_num:
    print('Yes')
    print(f'Sum = {eve_num}')
else:
    diff = abs(eve_num - odd_num)
    print('No')
    print(f'Diff = {diff}')