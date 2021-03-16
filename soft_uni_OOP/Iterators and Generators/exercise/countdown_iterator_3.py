class countdown_iterator:

    def __init__(self, count):
        self.count = count + 1
        self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration()
        self.count -= self.step
        return self.count



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")