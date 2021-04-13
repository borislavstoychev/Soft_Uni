from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    water = "Salt"

    def __init__(self, name: str):
        super().__init__(name, capacity=25)

    def add_fish(self, fish):
        if "SaltwaterFish" != fish.__class__.__name__:
            return "Water not suitable."
        return super().add_fish(fish)

