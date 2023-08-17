import unittest
from calculator.calculate import calculate
from utils import (
    OperationNode,
    generate_float,
    operation_node_to_result,
    operation_node_to_standard,
)


class CalculatorIntTest(unittest.TestCase):
    def test_number_in_bracket(self):
        number = generate_float()

        actual = calculate(str(number))

        self.assertEqual(actual, number)

    def test_operation_on_floats(self):
        operation = OperationNode(
            generate_float(),
            "+",
            OperationNode(generate_float(), "*", generate_float()),
        )
        value = operation_node_to_standard(operation)
        expected = operation_node_to_result(operation)

        actual = calculate(value)

        self.assertEqual(actual, expected, f"[the operation: {value}]")
