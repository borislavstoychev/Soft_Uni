def tags(tag):
    def inner(fn):
        def wrapper(*args):
            return f"<{tag}>{fn(*args)}</{tag}>"
        return wrapper
    return inner



@tags('p')
def join_strings(*args):
    return "".join(args)


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
print(join_strings("Hello", " you!"))