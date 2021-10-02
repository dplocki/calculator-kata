import unittest

def calculate(value):
    if value == '':
        return 0

    return int(value)

class Calculator(unittest.TestCase):
    def test_empty_string_should_return_zero(self):
        actual = calculate('')
        self.assertEqual(actual, 0)

    def test_single_number_return_that_number(self):
        actual = calculate('23')
        self.assertEqual(actual, 23)

if __name__ == '__main__':
    unittest.main()
