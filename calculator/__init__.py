from dataclasses import dataclass
import operator
import re
from typing import Generator, Union, Callable


@dataclass
class Operator:
    level: int
    function: Callable


@dataclass
class Bracket:
    opening: bool
    level: int = 0


OPERATORS = {
    "+": Operator(1, operator.add),
    "-": Operator(1, operator.sub),
    "*": Operator(2, operator.mul),
    "^": Operator(3, operator.pow),
}


BRACKETS = {"(": Bracket(True), ")": Bracket(False)}


class CalculateException(Exception):
    pass


def calculate_postfix_notation(tokens) -> Union[int, int]:
    stack = []

    for token in tokens:
        if type(token) == Operator:
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(token.function(number1, number2))
        else:
            stack.append(token)

    return stack.pop()


def convert_infix_into_postfix_notation(tokens):
    operators = []

    for token in tokens:
        if type(token) == int:
            yield token
        elif type(token) == Bracket:
            if token.opening:
                operators.append(token)
            else:
                while len(operators) > 0:
                    token = operators.pop()
                    if type(token) == Bracket and token.opening:
                        break

                    yield token
        else:
            while len(operators) > 0 and operators[-1].level > token.level:
                yield operators.pop()

            operators.append(token)

    while len(operators) > 0:
        yield operators.pop()


def split_input_string_to_tokens(
    input_value: str,
) -> Generator[str, None, None]:
    yield from filter(lambda token: token.strip() != "", re.split("(\W)", input_value))


def parse_tokens(tokens):
    expectedNumber = True
    for token in tokens:
        if token in OPERATORS and not expectedNumber:
            yield OPERATORS[token]
            expectedNumber = True
        elif token.isdigit() and expectedNumber:
            yield int(token)
            expectedNumber = False
        elif token in BRACKETS:
            yield BRACKETS[token]
        else:
            raise CalculateException(f"Unexpected token, got: {token}")


def calculate(input_value: str) -> int:
    if input_value == "":
        return 0

    return calculate_postfix_notation(
        convert_infix_into_postfix_notation(
            parse_tokens(split_input_string_to_tokens(input_value))
        )
    )
