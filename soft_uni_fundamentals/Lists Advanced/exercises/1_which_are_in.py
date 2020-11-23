line_1 = input().split(", ")
line_2 = input().split(", ")

result = list(dict.fromkeys(word_1 for word_1 in line_1 for wor_2 in line_2 if word_1 in wor_2))

print(result)
