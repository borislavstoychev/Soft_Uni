class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []    #animals for all vets; space (5 by default).

    def register_animal(self, animal_name):
        if self.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            self.space -= 1
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            self.space += 1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals.\n{self.space} space left in clinic"
