from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    water = "Fresh"

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3

