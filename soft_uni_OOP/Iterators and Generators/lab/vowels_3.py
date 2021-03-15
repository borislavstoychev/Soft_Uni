class vowels:

    def __init__(self, some_sting):
        self.some_string = some_sting
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index not in range(len(self.some_string)):
            raise StopIteration()
        letter = self.some_string[self.index]
        self.index += 1
        if letter.lower() in "aeiuyo":
            return letter
        return self.__next__()




my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)