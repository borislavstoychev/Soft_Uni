numbers = [num for num in range(int(input()), int(input()) + 1)]
divisible = [d for d in range(2, 11)]
print([n for n in numbers if any([n % x == 0 for x in divisible])])
