from dataclasses import dataclass
import random
from calculator.parsing import OPERATORS


def generate_int(maximum=99999):
    return random.randrange(1, maximum)


def generate_float(maximum=9999):
    return random.uniform(1, maximum)


def generate_operation():
    return random.choice(["-", "+", "*", "/"])


@dataclass
class OperationNode:
    left: None | type["OperationNode"] | int
    root: str | int
    right: None | type["OperationNode"] | int


def is_numeric_value(value: any) -> bool:
    return type(value) == int or type(value) == float


def operation_node_to_standard(node: OperationNode, previous_operator_level=-1) -> str:
    if is_numeric_value(node):
        return str(node)

    if is_numeric_value(node.root):
        return str(node.root)

    operator_level = OPERATORS[node.root].level
    left = (
        operation_node_to_standard(node.left, operator_level)
        if node.left != None
        else ""
    )
    right = (
        operation_node_to_standard(node.right, operator_level)
        if node.right != None
        else ""
    )
    result = f"{left} {node.root} {right}"

    if operator_level < previous_operator_level:
        result = f"({result})"

    return result


def operation_node_to_result(node: OperationNode) -> int:
    if is_numeric_value(node):
        return node

    if is_numeric_value(node.root):
        return node.root

    return OPERATORS[node.root].function(
        operation_node_to_result(node.left), operation_node_to_result(node.right)
    )
