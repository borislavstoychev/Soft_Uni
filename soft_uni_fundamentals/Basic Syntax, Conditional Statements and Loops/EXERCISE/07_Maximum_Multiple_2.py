num_1 = int(input())
num_2 = int(input())

for num in range(num_2, 0, -1):
    if num % num_1 == 0:
        print(num)
        break