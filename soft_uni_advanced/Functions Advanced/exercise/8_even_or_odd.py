def even_odd(*args, command=""):
    command = args[-1]
    nums = args[:-1]
    result = []
    if command == "odd":
        result = [n for n in nums if not n % 2 == 0]
    elif command == "even":
        result = [n for n in nums if n % 2 == 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
