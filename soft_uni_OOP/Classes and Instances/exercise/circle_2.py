class Circle:

    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = self.pi * self.radius ** 2
        area = float(f"{area:.2f}")
        return area

    def get_circumference(self):
        circumference = 2*self.pi * self.radius
        circumference = float(f"{circumference:.2f}")
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
