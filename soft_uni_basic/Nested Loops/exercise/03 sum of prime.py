line = input()
prime = 0
not_prime = 0

while line != 'stop':
    num = int(line)
    if num < 0:
        print(f'Number is negative.')
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2 or num == 1:
            prime += num
        else:
            not_prime += num
    line = input()
print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {not_prime}')