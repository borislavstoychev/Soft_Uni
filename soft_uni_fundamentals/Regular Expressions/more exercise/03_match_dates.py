import re

date = input()
pattern = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4}\b)"
matches = re.findall(pattern, date)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")