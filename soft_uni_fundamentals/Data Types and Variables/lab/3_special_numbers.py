n = int(input())

for number in range(1, n + 1):
    sum_of_digit = 0
    num = number

    while num > 0:
        digit = num % 10
        sum_of_digit += digit
        num = num // 10
        
    is_special = sum_of_digit == 5 or sum_of_digit == 7 or sum_of_digit == 11
    print(f'{number} -> {is_special}')
