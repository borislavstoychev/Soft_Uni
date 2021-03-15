class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0

    def __iter__(self):
        return self

    def __next__(self):
        for index in range(self.start, self.end):
            self.start += self.increment
            self.increment = 1
            return self.start
        raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)