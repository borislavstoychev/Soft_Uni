import re

line = input()
pattern = r"(^|(\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+\b"
while line:
    matches = re.finditer(pattern, line)
    [print(match.group()) for match in matches]
    line = input()