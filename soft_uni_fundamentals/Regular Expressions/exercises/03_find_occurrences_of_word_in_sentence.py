import re

line = input().lower()
word = input().lower()
pattern = fr"\b{word}\b"
matches = re.findall(pattern, line, re.IGNORECASE)
print(len(matches))
