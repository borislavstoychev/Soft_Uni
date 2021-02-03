import re


def write_result(r):
    with open("output.txt", "w") as file:
        return file.writelines("\n".join(r))


def get_file_counter(files):
    with open(files, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


def get_analyse(first, second):
    analyse = {}
    for word in first_words:
        if word in second_words:
            analyse[word] = second_words.count(word)
    return analyse


first_words = (get_file_counter("words.txt"))
second_words = (get_file_counter("text1.txt"))
analyse_dict = get_analyse(first_words, second_words)
result = ([f"{x[0]} - {x[1]}" for x in sorted(analyse_dict.items(), key=lambda el: -el[1])])
write_result(result)
