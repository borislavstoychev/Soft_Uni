import sys
data = input()

min_num = sys.maxsize

while data != 'Stop':
    num = int(data)

    if num < min_num:
        min_num = num
    data = input()

print(min_num)