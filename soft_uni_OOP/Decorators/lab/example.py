def increment_with(n):
    def inc(func):
        def increase(*args, **kwargs):
            return [num + n for num in func(*args, **kwargs)]

        return increase

    return inc


@increment_with(5)
def get_numbers():
    return [1, 2, 3, 4, 5]


print(get_numbers())
