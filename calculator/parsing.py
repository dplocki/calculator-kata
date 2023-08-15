from dataclasses import dataclass
import operator
import re
from typing import Callable, Generator, Iterable

from calculator.exceptions import CalculateException


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
    "/": Operator(2, operator.truediv),
    "^": Operator(3, operator.pow),
}


BRACKETS = {"(": Bracket(True), ")": Bracket(False)}


def convert_infix_into_postfix_notation(
    tokens: Iterable[int | Operator | Bracket],
) -> Generator[int | Operator | Bracket, None, None]:
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


def parse_tokens(
    tokens: Iterable[str],
) -> Generator[int | Operator | Bracket, None, None]:
    expectedNumber = True
    bracket_counter = 0
    negative = False

    for token in tokens:
        if token in OPERATORS and not expectedNumber:
            yield OPERATORS[token]
            expectedNumber = True
        elif token == "-" and expectedNumber:
            negative = True
        elif token.isdigit() and expectedNumber:
            number = int(token)
            if negative:
                number *= -1
                negative = False
            yield number
            expectedNumber = False
        elif token in BRACKETS:
            bracket = BRACKETS[token]

            if bracket_counter == 0 and not bracket.opening:
                raise CalculateException(
                    "Closing bracket, but there was no open before"
                )

            yield bracket
            bracket_counter += 1 if bracket.opening else -1
        else:
            raise CalculateException(f"Unexpected token, got: {token}")

    if bracket_counter != 0:
        raise CalculateException("Brackets (open/close) are not matching")
