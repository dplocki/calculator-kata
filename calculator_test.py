import unittest

def calculate(value):
    return 0

class Calculator(unittest.TestCase):
    def test_empty_string_should_return_zero(self):
        actual = calculate('')
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()
