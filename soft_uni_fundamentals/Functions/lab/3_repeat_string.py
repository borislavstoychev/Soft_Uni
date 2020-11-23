def repeat_string(line, n):
    new_string = ''
    for repeat in range(n):
        new_string += line
    return new_string


line_input = input()
nums = int(input())

print(repeat_string(line_input, nums))

