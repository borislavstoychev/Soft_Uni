import re

line = input()
pattern = r"(#|\|)(?P<name>[A-Za-z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"
total_calories = 0
for match in re.finditer(pattern, line):
    total_calories += int(match.group(4))
print(f"You have food to last you for: {total_calories // 2000} days!")
for match in re.finditer(pattern, line):
    print(f"Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}")