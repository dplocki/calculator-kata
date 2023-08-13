import unittest
from calculator import calculate
from utils import (
    OperationNode,
    generate_int,
    operation_node_to_result,
    operation_node_to_standard,
)


class CalculatorTest(unittest.TestCase):
    def test_empty_string_should_return_zero(self):
        actual = calculate("")

        self.assertEqual(actual, 0)

    def test_single_number_return_that_number(self):
        self._run_test(OperationNode(None, generate_int(), None))

    def test_two_add_operation(self):
        self._run_test(
            OperationNode(
                generate_int(), "+", OperationNode(generate_int(), "+", generate_int())
            )
        )

    def test_add_then_minus_operation(self):
        self._run_test(
            OperationNode(
                generate_int(), "+", OperationNode(generate_int(), "-", generate_int())
            )
        )

    def test_plus_and_multiple_operation(self):
        self._run_test(
            OperationNode(
                generate_int(), "+", OperationNode(generate_int(), "*", generate_int())
            )
        )

    def test_plus_and_power_operation(self):
        self._run_test(
            OperationNode(
                generate_int(),
                "+",
                OperationNode(generate_int(10), "^", generate_int(10)),
            )
        )

    def test_plus_power_multi_operation(self):
        self._run_test(
            OperationNode(
                generate_int(),
                "+",
                OperationNode(
                    OperationNode(generate_int(10), "^", generate_int(10)),
                    "*",
                    generate_int(100),
                ),
            )
        )

    def _run_test(self, operation):
        value = operation_node_to_standard(operation)
        expected = operation_node_to_result(operation)

        actual = calculate(value)
        print(value, expected, actual)
        self.assertEqual(actual, expected, f"[the operation: {value}]")
