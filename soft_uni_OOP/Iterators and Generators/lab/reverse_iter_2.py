class reverse_iter:

    def __init__(self, some_list):
        self.some_list = list(some_list)

    def __iter__(self):
        return self

    def __next__(self):
        while self.some_list:
            return self.some_list.pop()
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)