import re

line = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, line)
for match in matches:
    print(match.group(0), end=" ")