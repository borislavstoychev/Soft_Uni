word_snake = input()

word_matches = ["water", "sand", "sun", "fish"]
match = 0

for i in range(len(word_matches)):
    match += word_snake.lower().count(word_matches[i])

print(match)