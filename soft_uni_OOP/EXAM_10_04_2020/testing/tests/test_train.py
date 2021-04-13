from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.train = Train("Bobby", 5)

    def test_constructor(self):
        self.assertEqual("Bobby", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_raise_error(self):
        with self.assertRaises(ValueError) as vr:
            self.train.passengers = [1, 2, 3, 4, 5]
            self.train.add("Bobbi")
        self.assertEqual("Train is full", str(vr.exception))

    def test_add_passenger_name_in_train(self):
        with self.assertRaises(ValueError) as vr:
            self.train.add("Bobby")
            self.train.add("Bobby")

        self.assertEqual("Passenger Bobby Exists", str(vr.exception))

    def test_add_passenger(self):
        self.train.add("Added passenger Bobby")
        self.assertEqual(["Added passenger Bobby"], self.train.passengers)

    def test_remove_raise_error(self):
        with self.assertRaises(ValueError) as vr:
            self.train.remove("Bobby")
        self.assertEqual("Passenger Not Found", str(vr.exception))

    def test_remove(self):
        self.train.add("Bobby")
        self.assertEqual("Removed Bobby", self.train.remove("Bobby"))