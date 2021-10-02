import unittest
import random

def calculate(value):
    if value == '':
        return 0

    return int(value)

def generate_int():
    return random.randrange(0, 99999)

class Calculator(unittest.TestCase):
    def test_empty_string_should_return_zero(self):
        actual = calculate('')
        self.assertEqual(actual, 0)

    def test_single_number_return_that_number(self):
        number = generate_int()
        actual = calculate(str(number))
        self.assertEqual(actual, number)

if __name__ == '__main__':
    unittest.main()
