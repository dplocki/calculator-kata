from calculator import calculate
from utils import generate_int


import unittest


class CalculatorSupportedOperationsTest(unittest.TestCase):
    def test_single_add_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 + number2

        actual = calculate(f"{number1} + {number2}")

        self.assertEqual(actual, expected)

    def test_single_multiply_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 * number2

        actual = calculate(f"{number1} * {number2}")

        self.assertEqual(actual, expected)

    def test_single_subtraction_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 - number2

        actual = calculate(f"{number1} - {number2}")

        self.assertEqual(actual, expected)

    def test_single_power_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 ** number2

        actual = calculate(f"{number1} ^ {number2}")

        self.assertEqual(actual, expected)
