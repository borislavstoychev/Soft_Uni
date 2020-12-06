import re

input_data = input()

pattern_digits = r'\d'
pattern_emoji = r'(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1'

cool_threshold = 1
emojies = []
emojies_ascii = []

result_digits = re.findall(pattern_digits, input_data)
result_digits = [int(s) for s in result_digits]
for num in result_digits:
    cool_threshold *= num

result_emojis = re.finditer(pattern_emoji, input_data)
for emoji in result_emojis:
    emojies.append(emoji.group())
    emoji_cool = 0
    for i in range(len(emoji.group())):
        if emoji.group()[i] not in (':*'):
            emoji_cool += ord(emoji.group()[i])
    if emoji_cool >= cool_threshold:
        emojies_ascii.append(emoji.group())

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojies)} emojis found in the text. The cool ones are:')
print(*emojies_ascii, sep="\n")
