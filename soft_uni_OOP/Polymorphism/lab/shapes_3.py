from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass
        # return radios * radios * pi

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radios):
        self.__radios = radios

    def calculate_area(self):
        return self.__radios * self.__radios * pi

    def calculate_perimeter(self):
        return self.__radios * 2 * pi


class Rectangle(Shape):

    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def calculate_area(self):
        return self.__w * self.__h

    def calculate_perimeter(self):
        return self.__w * 2 + self.__h * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
