def reverse_text(string):
    i = -1
    range_of_string = len(string)
    while range_of_string:
        yield string[i]
        range_of_string -= 1
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
