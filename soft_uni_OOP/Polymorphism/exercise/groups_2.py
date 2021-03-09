class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group(list):

    def __init__(self, name, people):
        super().__init__(people)
        self.name = name

    @property
    def people(self):
        people = []
        for i in range(len(self)):
            people.append(super().__getitem__(i))
        return people

    def __str__(self):
        return f"Group {self.name} with members {', '.join(map(str, self.people))}"

    def __getitem__(self, index: int):
        return f"Person {index}: {self.people[index].__str__()}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group


print(len(first_group))
print(second_group)
print(third_group[0])
print(first_group.__getitem__(0))

for p in range(len(third_group)):
    print(third_group.__getitem__(p))