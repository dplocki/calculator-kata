from dataclasses import dataclass
import random
from calculator.parsing import OPERATORS


def generate_int(maximum=99999):
    return random.randrange(1, maximum)


def generate_operation():
    return random.choice(["-", "+", "*", "/"])


@dataclass
class OperationNode:
    left: None | type["OperationNode"] | int
    root: str | int
    right: None | type["OperationNode"] | int


def operation_node_to_standard(node: OperationNode, previous_operator_level=-1) -> str:
    if type(node) == int:
        return str(node)

    if type(node.root) == int:
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
    if type(node) == int:
        return node

    if type(node.root) == int:
        return node.root

    return OPERATORS[node.root].function(
        operation_node_to_result(node.left), operation_node_to_result(node.right)
    )
