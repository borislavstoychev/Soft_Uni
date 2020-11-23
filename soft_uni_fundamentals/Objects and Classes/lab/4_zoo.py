class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, names):
        if species == "mammal":
            self.mammals.append(names)
        elif species == "fish":
            self.fishes.append(names)
        elif species == "bird":
            self.birds.append(names)
        Zoo.__animals += 1

    def get_info(self, info):
        result = ''
        if info == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif info == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif info == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}\n"
        return result + f'Total animals: {Zoo.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())

for _ in range(number):
    line = input()
    species, name = line.split()
    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))
