class HashTable:

    def __init__(self, capacity=4):
        self.__keys = [None] * capacity
        self.__values = [None] * capacity
        self.capacity = capacity

    @property
    def keys(self):
        return self.__keys

    @property
    def values(self):
        return self.__values

    def __getitem__(self, key):
        idx = self.__keys.index(key)
        return self.__values[idx]

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        if self.actual_length == self.capacity:
            self.__increase_size()
        index = self.__hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __increase_size(self):
        self.__keys = self.__keys + [None] * self.capacity
        self.__values = self.__values + [None] * self.capacity
        self.capacity *= 2

    def __check_available_index(self, index):
        if index == len(self.__keys):
            return self.__check_available_index(0)
        if self.__keys[index] is None:
            return index
        return self.__check_available_index(index + 1)

    def __hash(self, key):
        index = sum([ord(char) for char in key]) % self.capacity
        available_index = self.__check_available_index(index)
        return available_index

    def __len__(self):
        return self.capacity

    @property
    def actual_length(self):
        return len([k for k in self.__keys if k is not None])

    def __repr__(self):
        result = [f"{self.__keys[index]}: {self.__values[index]}" for index in range(len(self.__keys)) if self.__keys[index] is not None]
        return '{' + ", ".join(result) + '}'

    def add(self, key, value):
        self[key] = value




# table = HashTable()
# table["name"] = "Peter"
# table["age"] = 25
# table["age"] = 26
# table.add("Bobby", "30")
#
# print(table)
# print(table["name"])
# print(table["age"])
# print(len(table))
# print(table.actual_length)

