text = list(input())
text_dict = {}
for i in range(len(text)):
    if not text[i] == " ":
        if text[i] not in text_dict:
            text_dict[text[i]] = 0
        text_dict[text[i]] += 1
for (key, value) in text_dict.items():
    print(f"{key} -> {value}")
