from sys import maxsize
num_1 = int(input())
num_2 = int(input())
max_num = -maxsize
for i in range(num_1, num_2 + 1):
    if i % num_1 == 0:
        if i > max_num:
            max_num = i
print(max_num)

