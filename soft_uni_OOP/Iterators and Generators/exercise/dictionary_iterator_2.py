class dictionary_iter:

    def __init__(self, my_dict: dict):
        self.my_dict = dict(my_dict)

    def __iter__(self):
        return self

    def __next__(self):
        while self.my_dict:
            key = next(iter(self.my_dict))
            value = self.my_dict[key]
            self.my_dict.pop(key)
            return key, value
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
