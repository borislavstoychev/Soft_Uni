width = int(input())
length = int(input())

cake_size = width * length
line = input()
count_peaces = 0
while cake_size > 0 and line != 'STOP':
    num_of_cake_peaces = int(line)
    cake_size -= num_of_cake_peaces
    if cake_size <= 0:
        break
    line = input()
if cake_size < 0:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')
else:
    print(f'{cake_size - count_peaces} pieces are left.')
