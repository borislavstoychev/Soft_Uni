def multiply(times):

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return [num * times for num in func(*args, **kwargs)]
            except TypeError:
                return func(*args, **kwargs) * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return [num + 10 for num in number]


print(add_ten([6, 3]))
