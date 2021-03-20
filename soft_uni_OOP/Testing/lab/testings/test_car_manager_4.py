from car_manager_4 import Car
import unittest


class CarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car(2007, "Mercedes", 10, 70)

    def test_constructor(self):
        self.assertEqual(2007, self.car.make)
        self.assertEqual("Mercedes", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_set(self):
        self.car.make = 2008
        self.assertEqual(2008, self.car.make)

    def test_make_set_with_null(self):
        with self.assertRaises(Exception):
            self.car.make = 0
            self.car.make = ""

    def test_model_set(self):
        self.car.model = "Audi"
        self.assertEqual("Audi", self.car.model)

    def test_model_set_with_null_or_empty(self):
        with self.assertRaises(Exception):
            self.car.model = 0
            self.car.model = ""

    def test_fuel_consumption_set(self):
        self.car.fuel_consumption = 15
        self.assertEqual(15, self.car.fuel_consumption)

    def test_fuel_consumption_set_with_null(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0
            self.car.fuel_consumption = -1

    def test_fuel_capacity_set(self):
        self.car.fuel_capacity = 60
        self.assertEqual(60, self.car.fuel_capacity)

    def test_fuel_capacity_set_with_null(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0
            self.car.fuel_capacity = -1

    def test_fuel_amount_set(self):
        self.car.fuel_amount = 20
        self.assertEqual(20, self.car.fuel_amount)

    def test_negative_fuel_amount_(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -20

    def test_negative_refuel(self):
        with self.assertRaises(Exception):
            self.car.refuel(-20)
            self.car.refuel(0)

    def test_refuel_bigger_amount(self):
        self.car.refuel(100)
        self.assertEqual(70, self.car.fuel_amount)

    def test_refuel_amount(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_drive_too_long(self):
        with self.assertRaises(Exception):
            self.car.drive(200000)

    def test_drive(self):
        self.car.refuel(100)
        self.car.drive(200)
        self.assertEqual(50, self.car.fuel_amount)



if __name__ == "__main__":
    unittest.main()
