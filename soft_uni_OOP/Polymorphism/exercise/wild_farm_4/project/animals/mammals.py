from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed




class Mouse(Mammal):
    TYPE_OF_FOODS = (Vegetable, Fruit)
    INCREASE_WEIGHT = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    TYPE_OF_FOODS = (Meat,)
    INCREASE_WEIGHT = 0.40

    @staticmethod
    def make_sound():
        return "Woof"


class Cat(Mammal):
    TYPE_OF_FOODS = (Vegetable, Meat)
    INCREASE_WEIGHT = 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    TYPE_OF_FOODS = (Meat,)
    INCREASE_WEIGHT = 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
