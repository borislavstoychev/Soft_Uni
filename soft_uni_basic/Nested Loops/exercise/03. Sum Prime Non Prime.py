line = input()
prime = 0
not_prime = 0
while line != 'stop':
    num = int(line)
    if num < 0:
        print(f'Number is negative.')
    elif num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_prime += num
                break
        else:
            prime += num

    line = input()
print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {not_prime}')