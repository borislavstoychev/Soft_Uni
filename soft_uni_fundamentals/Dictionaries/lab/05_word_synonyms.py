synonym_word = {}
for index in range(int(input())):
    word = input()
    synonym = input()
    if word not in synonym_word:
        synonym_word[word] =[]
    synonym_word[word].append(synonym)
for word in synonym_word:
    print(f"{word} - {', '.join(synonym_word[word])}")



