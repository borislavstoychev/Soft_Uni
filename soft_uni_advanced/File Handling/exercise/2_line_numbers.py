import re


def marks_and_letters(line):
    letter_pattern = r"[a-z]"
    mark_pattern = r"[',\.\!\?-]"
    return len(re.findall(letter_pattern, line)), len(re.findall(mark_pattern, line))


with open("text.txt", "r") as file:
    lines = file.readlines()
    count = 0
    for l in lines:
        count += 1
        letters, marks = marks_and_letters(l.lower())
        print(f"Line {count}: {l.strip()} ({letters})({marks})")
