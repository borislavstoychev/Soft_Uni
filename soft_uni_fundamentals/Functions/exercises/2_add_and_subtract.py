def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract_number(r, num3):
    result = r - num3
    return result


def add_and_subtract(a):
    print(a)


n1 = int(input())
n2 = int(input())
n3 = int(input())

add_and_subtract(subtract_number(sum_numbers(n1, n2), n3))

