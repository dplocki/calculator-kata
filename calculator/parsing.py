from dataclasses import dataclass
import operator
import re
from typing import Callable, Generator, Iterable

from calculator.exceptions import CalculateException


@dataclass
class Operator:
    level: int
    function: Callable
    parameters_count: int = 2


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
    "neg": Operator(4, operator.neg, 1),
}


BRACKETS = {"(": Bracket(True), ")": Bracket(False)}


def convert_infix_into_postfix_notation(
    tokens: Iterable[int | Operator | Bracket],
) -> Generator[int | Operator | Bracket, None, None]:
    operators = []

    for token in tokens:
        if type(token) == int:
            yield token
        elif type(token) == float:
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
    yield from filter(
        lambda token: token != None and token.strip() != "",
        re.split(
            r"(\d+\.\d+[eE][\+\-]\d+)|(\d+\.\d+)|(\d+)|([\(\)\-+*/^])", input_value
        ),
    )


def parse_tokens(
    tokens: Iterable[str],
) -> Generator[int | Operator | Bracket, None, None]:
    pattern = re.compile(r"^\d+\.\d+([eE][\+\-]\d+)?$")
    expectedNumber = True
    bracket_counter = 0

    for token in tokens:
        if token in OPERATORS and not expectedNumber:
            yield OPERATORS[token]
            expectedNumber = True
        elif token == "-" and expectedNumber:
            yield OPERATORS["neg"]
        elif token.isdigit() and expectedNumber:
            yield int(token)
            expectedNumber = False
        elif pattern.match(token) and expectedNumber:
            yield float(token)
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
