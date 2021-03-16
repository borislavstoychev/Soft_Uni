class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = - step
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.index in range(self.count):
            self.num += self.step
            self.index += 1
            return self.num
        raise StopIteration()



numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)

for number in numbers:
    print(number)
