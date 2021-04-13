from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration != "None":
                aquarium[0].add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        try:
            aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
            # if aquarium.water != fish.water:
            #     return "Water not suitable."
            return aquarium.add_fish(fish)
        except IndexError:
            return

    def feed_fish(self, aquarium_name: str):
        try:
            aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"
        except IndexError:
            return

    def calculate_value(self, aquarium_name: str):
        try:
            aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
            value = sum(f.price for f in aquarium.fish)
            value += sum(d.price for d in aquarium.decorations)
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."
        except IndexError:
            return

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return "\n".join(result)

