from abc import ABC,abstractmethod


class Shapes(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        ...


class Rectangle(Shapes):

    def area(self):
        return self.width * self.height


class Triangle(Shapes):

    def area(self):
        return (self.width * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)