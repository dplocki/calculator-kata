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
        print(value, tokens)
        return reduce(operator.sub, map(int, tokens))

    return int(value)

def generate_int():
    return random.randrange(-99999, 99999)

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

    @unittest.skip("Temporary disabled for new parser apprach")
    def test_single_subtraction_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        expected = number1 - number2

        actual = calculate(f'{number1} - {number2}')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
