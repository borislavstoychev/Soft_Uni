from worker_1 import Worker
import unittest


class WorkerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Bobby", 999, 99)

    def test_initialized(self):
        self.assertEqual(self.worker.name, "Bobby")
        self.assertEqual(self.worker.salary, 999)
        self.assertEqual(self.worker.energy, 99)
        self.assertEqual(0, self.worker.money)

    def test_increment_energy(self):
        self.worker.rest()
        self.assertEqual(100, self.worker.energy)

    def test_raise_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_increase_money_by_salary(self):

        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)
        self.worker.work()
        self.assertEqual(self.worker.salary*2, self.worker.money)

    def test_decrease_energy(self):
        energy = self.worker.energy
        self.worker.work()
        self.assertEqual(energy - 1, self.worker.energy)

    def test_workerGetInfo(self):

        expected = f'{self.worker.name} has saved 0 money.'
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
