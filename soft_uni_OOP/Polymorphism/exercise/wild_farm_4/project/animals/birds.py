from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    WEIGHT_INCREASE = 0.25
    FOOD = (Meat, )

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    WEIGHT_INCREASE = 0.35
    FOOD = (Vegetable, Fruit, Meat, Seed)

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

