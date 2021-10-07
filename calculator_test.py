import unittest
import random
import operator
from functools import reduce

def calculate(value):
    if value == '':
        return 0

    if '+' in value:
        tokens = value.split('+')
        return sum(map(int, tokens))

    if '-' in value:
        tokens = value.split('-')
        return reduce(operator.sub, map(int, tokens))

    return int(value)

def generate_int():
    return random.randrange(0, 99999)

def generate_operation():
    return random.choice(['-', '+', '*', '/'])

class CalculatorTest(unittest.TestCase):

    def test_empty_string_should_return_zero(self):
        actual = calculate('')
        self.assertEqual(actual, 0)

    def test_single_number_return_that_number(self):
        number = generate_int()
        actual = calculate(str(number))
        self.assertEqual(actual, number)

    def test_single_add_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 + number2

        actual = calculate(f'{number1} + {number2}')
        self.assertEqual(actual, expected)

    def test_single_subtraction_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 - number2

        actual = calculate(f'{number1} - {number2}')
        self.assertEqual(actual, expected)

class PolishNotationParser():
    
    def parse(self, value):
        if value == '':
            return []

        tokens = value.split()
        if len(tokens) == 1:
            return [int(tokens[0])]

        return [tokens[1], int(tokens[0]), int(tokens[2])]

class PolishNotationParserTests(unittest.TestCase):

    def setUp(self):
        self.parser = PolishNotationParser()

    def test_empty_string(self):
        actual = self.parser.parse('')
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
        
        actual = self.parser.parse(f'{number1} {operation} {number2}')

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
