def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = [func_name(*data) for func_name, data in args]
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))