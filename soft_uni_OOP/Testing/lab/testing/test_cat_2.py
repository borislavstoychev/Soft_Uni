import unittest
from cat_2 import Cat



class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Fluffy")

    def test_size_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_feed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_cannot_eat_if_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cannot_fall_asleep_if_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)



if __name__ == '__main__':
    unittest.main()
