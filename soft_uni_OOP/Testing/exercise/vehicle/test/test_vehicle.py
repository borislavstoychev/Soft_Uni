from project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(25.5, 224.0)

    def test_vehicle_initialized(self):
        self.assertEqual(25.5, self.vehicle.fuel)
        self.assertEqual(25.5, self.vehicle.capacity)
        self.assertEqual(224.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(13, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(30)
        self.assertEqual(ex.exception.args[0], "Not enough fuel")

    def test_refuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(10, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)
        self.assertEqual(ex.exception.args[0], "Too much fuel")

    def test_str_vehicle(self):
        expect = "The vehicle has 224.0 horse power with 25.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expect, self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()

