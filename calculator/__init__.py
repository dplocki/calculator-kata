import operator
import re
from typing import Generator, Union


class Operator:
    def __init__(self, level, function) -> None:
        self.level = level
        self.function = function

    def __repr__(self) -> str:
        return str(self.function)


OPERATORS = {
    "+": Operator(1, operator.add),
    "-": Operator(1, operator.sub),
    "*": Operator(2, operator.mul),
    "^": Operator(3, operator.pow),
}


class CalculateException(Exception):
    pass


def calc(tokens) -> Union[int, int]:
    stack = []

    for token in tokens:
        if type(token) == Operator:
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(token.function(number1, number2))
        else:
            stack.append(token)

    return stack.pop()


def convert_tokens_into_infix_notation(tokens):
    operators = []

    for token in tokens:
        if type(token) == int:
            yield token
        else:
            while len(operators) > 0 and operators[-1].level > token.level:
                yield operators.pop()

            operators.append(token)

    while len(operators) > 0:
        yield operators.pop()


def calculate(input_value: str) -> int:
    def split_input_string_to_tokens(
        input_value: str,
    ) -> Generator[str, None, None]:
        yield from filter(
            lambda token: token.strip() != "", re.split("(\W)", input_value)
        )

    def parse_tokens(tokens):
        expectedNumber = True
        for token in tokens:
            if token in OPERATORS and not expectedNumber:
                yield OPERATORS[token]
                expectedNumber = True
            elif token.isdigit() and expectedNumber:
                yield int(token)
                expectedNumber = False
            else:
                raise CalculateException(f"Unexpected token, got: {token}")

    if input_value == "":
        return 0

    return calc(
        convert_tokens_into_infix_notation(
            parse_tokens(split_input_string_to_tokens(input_value))
        )
    )
