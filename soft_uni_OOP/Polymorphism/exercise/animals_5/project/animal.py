from abc import ABC, abstractmethod


class Animal(ABC):
    name: str
    age: int
    gender: str

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        ...

    @abstractmethod
    def make_sound(self):
        ...






