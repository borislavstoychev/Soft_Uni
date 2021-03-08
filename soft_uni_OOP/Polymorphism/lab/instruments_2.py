import unittest


class InstrumentsTest(unittest.TestCase):
    def test(self):
        class Test:
            def play(self):
                return "test"

        res = play_instrument(Test())
        self.assertEqual(res, "test")


if __name__ == '__main__':
    unittest.main()


def play_instrument(instrument):
    return instrument.play()
