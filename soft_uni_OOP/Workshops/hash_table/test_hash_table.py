from hash_table import HashTable
from unittest import TestCase, main


class HashTableTest(TestCase):

    def setUp(self) -> None:
        self.hash_table = HashTable()

    def test_attributes(self):
        self.assertEqual(4, len(self.hash_table.keys))
        self.assertEqual(4, len(self.hash_table.values))
        self.assertEqual(4, self.hash_table.capacity)

    def test_with_available_space(self):
        self.hash_table.add("Bobby", "5")
        self.assertEqual(1, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.capacity)
        self.assertEqual("5", self.hash_table["Bobby"])

    def test_without_available_space_increase_size(self):
        for number in range(1, self.hash_table.capacity + 1):
            self.hash_table.add(f"test_{number}", f"value_{number}")
        self.assertEqual(4, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.capacity)
        self.hash_table.add("test_5", "value_5")
        self.assertEqual(5, self.hash_table.actual_length)
        self.assertEqual(8, self.hash_table.capacity)
        self.assertIn("test_5", self.hash_table.keys)

    def test_value_replaced_if_key_exist(self):
        self.hash_table.add("Bobby", "5")
        self.assertEqual("5", self.hash_table["Bobby"])
        self.hash_table["Bobby"] = "6"
        self.assertEqual("6", self.hash_table["Bobby"])

    def test_get_existing_key(self):
        self.hash_table.add("Bobby", "5")
        self.assertEqual("5", self.hash_table.get("Bobby"))

    def test_get_no_existing_key(self):
        self.hash_table.add("Bobby", "5")
        self.assertIsNone(self.hash_table.get("B"))

    def test_representation(self):
        self.hash_table.add("Bobby", "5")
        self.assertEqual("{Bobby: 5}", str(self.hash_table))


