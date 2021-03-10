from abc import ABC, abstractmethod


class Animal(ABC):

    FOOD = None
    WEIGHT_INCREASE = None

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def feed(self, food):
        if not isinstance(food, self.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

    @abstractmethod
    def make_sound(self):
        ...


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"