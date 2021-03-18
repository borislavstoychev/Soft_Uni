def type_check(check):
    def inner(fn):
        def wrapper(*args):
            if all(isinstance(a, check) for a in args):
                return fn(*args)
            return "Bad Type"
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num*2


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
print(times2(2))
print(times2('Not A Number'))