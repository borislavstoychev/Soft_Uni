from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    water = "Fresh"

    def __init__(self, name: str):
        super().__init__(name, 50)

    def add_fish(self, fish):
        if "FreshwaterFish" != fish.__class__.__name__:
            return "Water not suitable."
        return super().add_fish(fish)
