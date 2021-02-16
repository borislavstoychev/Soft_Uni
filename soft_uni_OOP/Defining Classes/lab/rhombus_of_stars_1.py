def print_rhombus(n: int):
    growing: int = 1
    shrinking: int = -1

    def print_line(i: int, direction: int):
        if i == 0:
            return
        line = " " * (n - i) + "* " * i
        print(line.rstrip())
        if i == n:
            direction = shrinking
        print_line(i + direction, direction)
    print_line(1, growing)


print_rhombus(int(input()))
