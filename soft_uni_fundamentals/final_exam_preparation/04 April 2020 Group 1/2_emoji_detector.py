import re

line = input()
pattern = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1"
emojis = [match.group() for match in re.finditer(pattern, line)]
cool_numbers = re.findall(r"\d", line)
cool_threshold = 1
emoji_coolness = {}
coolness = 0
for number in cool_numbers:
    cool_threshold *= int(number)
for emoji in emojis:
    coolness = 0
    for digit in emoji:
        if digit.isalpha():
            coolness += ord(digit)
    emoji_coolness[emoji] = coolness
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_coolness)} emojis found in the text. The cool ones are:")
[print(key) for (key, value) in emoji_coolness.items() if value > cool_threshold]
