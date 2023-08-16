import unittest
from calculator import calculate
from utils import generate_int


class CalculatorParserTest(unittest.TestCase):
    def test_should_accept_no_spaces(self):
        number1 = generate_int()
        number2 = generate_int()
        excepted = number1 + number2

        result = calculate(f"{number1}+{number2}")

        self.assertEqual(result, excepted)

    def test_should_accept_negative_numbers_in_brackets(self):
        number1 = generate_int()
        number2 = generate_int()
        excepted = number1 - number2

        result = calculate(f"{number1}+(-{number2})")

        self.assertEqual(result, excepted)

    def test_should_accept_negative_numbers_in_brackets(self):
        number1 = generate_int()
        number2 = generate_int()

        excepted = -1 * (number1 + number2)

        result = calculate(f"-({number1} + {number2})")

        self.assertEqual(result, excepted)
