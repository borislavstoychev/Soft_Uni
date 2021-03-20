from list_3 import IntegerList
import unittest


class IntegerListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4, 5)

    def test_constructor(self):
        self.assertIsInstance(all(self.list.get_data()), int)
        self.assertEqual([1, 2, 3, 4, 5,], self.list.get_data())

    def test_add_operation(self):
        self.list.add(6)
        expect = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expect, self.list.get_data())

    def test_add_operation_not_integer(self):
        with self.assertRaises(Exception):
            self.list.add("6")

    def test_remove_index(self):
        self.list.remove_index(-1)
        expect = [1, 2, 3, 4]
        self.assertEqual(expect, self.list.get_data())

    def test_remove_index_out_of_range(self):
        with self.assertRaises(Exception):
            self.list.remove_index(5)

    def test_get(self):
        self.assertEqual(5, self.list.get(4))

    def test_get_out_of_range(self):
        with self.assertRaises(Exception):
            self.list.get(5)

    def test_insert(self):
        self.list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.list.get_data())

    def test_insert_index_out_of_range(self):
        with self.assertRaises(Exception):
            self.list.insert(5, 6)

    def test_insert_element_not_int(self):
        with self.assertRaises(Exception):
            self.list.insert(4, "6")

    def test_get_biggest(self):
        self.assertEqual(max(self.list.get_data()), self.list.get_biggest())

    def test_get_index(self):
        self.assertEqual(self.list.get_data().index(5), self.list.get_index(5))




if __name__ == '__main__':
    unittest.main()