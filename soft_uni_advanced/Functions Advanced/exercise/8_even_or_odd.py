def even_odd(*args, command=""):
    command = args[-1]
    args = args[:-1]
    result = []
    if command == "odd":
        result = [int(n) for n in args if not int(n) % 2 == 0]
    elif command == "even":
        result = [int(n) for n in args if int(n) % 2 == 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
