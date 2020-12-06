import re

line = input()
pattern = r"(^_{1}|(?<=\s_){1})[A-Za-z0-9]+($|(?=[\s\.]))"
matches = re.finditer(pattern, line)
numbers = [match[0] for match in matches]
print(*numbers, sep=",")