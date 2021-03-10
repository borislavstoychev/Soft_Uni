from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    TYPE_OF_FOODS = (Meat,)
    INCREASE_WEIGHT = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    TYPE_OF_FOODS = (Vegetable, Fruit, Meat, Seed)
    INCREASE_WEIGHT = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
