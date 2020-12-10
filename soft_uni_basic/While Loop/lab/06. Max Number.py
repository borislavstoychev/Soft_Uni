import sys
data = input()

max_num = -sys.maxsize

while data != 'Stop':
    num = int(data)

    if num > max_num:
        max_num = num
    data = input()

print(max_num)