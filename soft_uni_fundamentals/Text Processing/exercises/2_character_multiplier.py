line = input().split()
summary = 0
max_word = ""
if len(line[0]) > len(line[1]):
    max_word = line[0]
else:
    max_word = line[1]
for index in range(len(max_word)):
    if index < len(line[0]) and index < len(line[1]):
        summary += ord(line[0][index]) * ord(line[1][index])
    else:
        summary += ord(max_word[index])
print(summary)