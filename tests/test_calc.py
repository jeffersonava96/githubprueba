import unittest
from main import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc('+', 1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc('-', 5, 2), 3)

    def test_mul(self):
        self.assertEqual(calc('*', 3, 4), 12)

    def test_div(self):
        self.assertEqual(calc('/', 8, 2), 4)

    def test_div_by_zero(self):
        self.assertIsNone(calc('/', 1, 0))

    def test_invalid_op(self):
        self.assertIsNone(calc('%', 1, 2))


if __name__ == '__main__':
    unittest.main()
