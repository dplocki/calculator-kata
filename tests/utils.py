from dataclasses import dataclass
import random
from calculator import OPERATORS


def generate_int(maximum=99999):
    return random.randrange(1, maximum)


def generate_operation():
    return random.choice(["-", "+", "*", "/"])


@dataclass
class OperationNode:
    left: None | type["OperationNode"] | int
    root: str | int
    right: None | type["OperationNode"] | int


def operation_node_to_standard(node: OperationNode) -> str:
    if type(node) == int:
        return str(node)

    if type(node.root) == int:
        return str(node.root)

    left = operation_node_to_standard(node.left) if node.left != None else ""
    right = operation_node_to_standard(node.right) if node.right != None else ""

    return f"{left} {node.root} {right}"


def operation_node_to_result(node: OperationNode) -> int:
    if type(node) == int:
        return node

    if type(node.root) == int:
        return node.root

    return OPERATORS[node.root].function(
        operation_node_to_result(node.left), operation_node_to_result(node.right)
    )
