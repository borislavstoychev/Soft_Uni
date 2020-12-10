import sys
n = int(input())
sum = 0
max_num = -sys.maxsize

for i in range(0, n):
    num = int(input())
    sum += num
    if num > max_num:
        max_num = num
sum -= max_num
if sum == max_num:
    print(f'Yes\n Sum = {sum}')
else:
    print(f'No\n Diff = {abs(max_num - sum)}')
