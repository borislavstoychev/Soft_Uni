from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    increasing_fuel_consumption = 0.9

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Car.increasing_fuel_consumption)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    increasing_fuel_consumption = 1.6
    fuel_loss = 0.95

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Truck.increasing_fuel_consumption)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.fuel_loss


if __name__ == "__main__":
    def test_car():
        car = Car(20, 5)
        car.drive(3)
        assert car.fuel_quantity == 2.299999999999997, car.fuel_quantity
        print("test passed")
        car.refuel(10)
        assert car.fuel_quantity == 12.299999999999997, car.fuel_quantity
        print("test passed")

    def test_truck():
        truck = Truck(100, 15)
        truck.drive(5)
        assert truck.fuel_quantity == 17.0, truck.fuel_quantity
        print("test passed")
        truck.refuel(50)
        assert truck.fuel_quantity == 64.5, truck.fuel_quantity
        print("test passed")

    test_car()
    test_truck()



