class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.letter = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.number:
            if self.letter >= len(self.sequence) - 1:
                self.letter = -1
            self.letter += 1
            self.number -= 1
            return self.sequence[self.letter]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')