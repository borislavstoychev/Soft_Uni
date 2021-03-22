from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Bobby", "dog", "bau")

    def test_constructor(self):
        self.assertEqual("Bobby", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bau", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expect = "Bobby makes bau"
        self.assertEqual(expect, self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_repr(self):
        expect = "Bobby is of type dog"
        self.assertEqual(expect, self.mammal.info())



if __name__ == "__main__":
    unittest.main()