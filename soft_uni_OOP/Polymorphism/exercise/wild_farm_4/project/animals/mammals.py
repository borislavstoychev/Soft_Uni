from project.animals.animal import Mammal
from project.food import Fruit, Meat, Vegetable


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10
    FOOD = (Vegetable, Fruit)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40
    FOOD = (Meat,)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30
    FOOD = (Vegetable, Meat)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00
    FOOD = (Meat,)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"
