def perfect_number(number):
    # num = 1
    # for i in range(2, number // 2 + 1):
    #     if number % i == 0:
    #         num += i
    # if num == number:
    #     print("We have a perfect number!")
    # else:
    #     print("It's not so perfect.")
    n = 1
    is_perfect = False
    while n <= limit:
        summary = 0
        divisor = 1
        while divisor < n:
            if not n % divisor:
                summary += divisor
            divisor = divisor + 1
        if summary == n:
            is_perfect = True

        n = n + 1
    if not is_perfect:
        print("It's not so perfect.")
    else:
        print("We have a perfect number!")


limit = int(input())

perfect_number(limit)
