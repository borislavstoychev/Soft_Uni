from abc import ABC, abstractmethod


class Animal(ABC):

    TYPE_OF_FOODS = tuple()
    INCREASE_WEIGHT = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def feed(self, food):
        if not isinstance(food, self.TYPE_OF_FOODS):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.INCREASE_WEIGHT
        self.food_eaten += food.quantity

    @abstractmethod
    def make_sound(self):
        ...


class Bird(Animal):

    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def make_sound(self):
        ...

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def make_sound(self):
        ...

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
