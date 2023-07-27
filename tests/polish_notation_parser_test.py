from calculator.PolishNotationParser import PolishNotationParser
from utils import generate_int, generate_operation
import unittest


class PolishNotationParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = PolishNotationParser()

    def test_empty_string(self):
        actual = self.parser.parse("")
        expected = []

        self.assertEqual(actual, expected)

    def test_single_number_string(self):
        number = generate_int()
        actual = self.parser.parse(str(number))

        self.assertEqual(actual, [number])

    def test_single_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        operation = generate_operation()

        expected = [operation, number1, number2]

        actual = self.parser.parse(f"{number1} {operation} {number2}")

        self.assertEqual(actual, expected)
