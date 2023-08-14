import unittest
from calculator import CalculateException, calculate
from utils import generate_int


class CalculatorValidationTest(unittest.TestCase):
    def test_throw_error_when_two_operators_next_to_each_other(self):
        number = generate_int()

        with self.assertRaises(CalculateException):
            calculate(f"++ {number}")

    def test_throw_error_when_two_numbers_next_to_each_other(self):
        number1 = generate_int()
        number2 = generate_int()
        number3 = generate_int()

        with self.assertRaises(CalculateException):
            calculate(f"{number1} + {number2} {number3}")

    def test_throw_error_when_provided_nonexisting_operator(self):
        number1 = generate_int()
        number2 = generate_int()

        with self.assertRaises(CalculateException):
            calculate(f"{number1} $ {number2}")

    def test_throw_error_when_provided_incorrect_number(self):
        number1 = generate_int()
        number2 = generate_int()

        with self.assertRaises(CalculateException):
            calculate(f"{number1} + {number2}abc")

    def test_throw_error_when_provided_single_brackets(self):
        number1 = generate_int()
        number2 = generate_int()

        with self.assertRaises(CalculateException):
            calculate(f"{number1} + ({number2}")
