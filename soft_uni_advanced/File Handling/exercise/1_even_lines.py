import re


def replace(line):
    return re.sub(r"[,\.\!\?-]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_number in range(len(lines)):
        if row_number % 2 == 0:
            replaced = replace(lines[row_number]).split()
            print(" ".join(replaced[::-1]))
