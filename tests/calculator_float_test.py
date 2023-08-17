import unittest
from calculator.calculate import calculate
from utils import (
    generate_float,
)


class CalculatorIntTest(unittest.TestCase):
    def test_number_in_bracket(self):
        number = generate_float()

        actual = calculate(str(number))

        self.assertEqual(actual, number)
