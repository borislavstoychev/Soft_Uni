def odd_and_even_sum(line):
    even_sum = 0
    odd_sum = 0
    for i in line:
        num = int(i)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()

odd_and_even_sum(number)

