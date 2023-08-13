import random
from typing import Union


def generate_int():
    return random.randrange(0, 99999)


def generate_operation():
    return random.choice(["-", "+", "*", "/"])


class OperationNode:
    def __init__(self, root=None, left=None, right=None) -> None:
        self.root = root
        self.left = left
        self.right = right

    def set_root(self, value):
        self.root = value

    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

    def __repr__(self) -> str:
        return f"Operation: {self.left} {self.root} {self.right}"


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

    left = operation_node_to_result(node.left) if node.left != None else ""
    right = operation_node_to_result(node.right) if node.right != None else ""

    if node.root == "+":
        return left + right
    elif node.root == "-":
        return left - right
    elif node.root == "*":
        return left * right
    elif node.root == "^":
        return left ** right

    raise Exception(f"Unknown {node.root}")
