VOWELS = {"a", "e", "o", "u", "y", "i"}


def vowel_filter(function):

    def wrapper(*args, **kwargs):
        return [letter for letter in function(*args, **kwargs) if letter.lower() in VOWELS]

    return wrapper



@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())