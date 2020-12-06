def take_odd(l):
    result = ""
    for i in range(1, len(l), 2):
        result += l[i]
    print(result)
    return result


def cut(l, i, length):
    result = l[:i] + l[i + length:]
    print(result)
    return result


def subst(l, substring, substitute):
    result = l.replace(substring, substitute)
    if result == l:
        print("Nothing to replace!")
    else:
        print(result)
    return result


line = input()
commands = input()
while not commands == "Done":
    if commands == "TakeOdd":
        line = take_odd(line)
    else:
        command, token1, token2 = commands.split()[::]
        if command == "Cut":
            index = int(token1)
            length = int(token2)
            line = cut(line, index, length)
        elif command == "Substitute":
            substring, substitute = token1, token2
            line = subst(line, substring, substitute)

    commands = input()
print(f"Your password is: {line}")
