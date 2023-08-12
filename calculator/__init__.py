import re
from typing import Generator


class CalculateException(Exception):
    pass


def parse_input_string_to_tokens(
    input_value: str,
) -> Generator[str, None, None]:
    yield from filter(lambda token: token.strip() != "", re.split("([+\-*/ ])", input_value))


def isdigit(number: str) -> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False


def calculate(input_value: str) -> float:
    if input_value == "":
        return 0

    operators = []
    numbers = []
    wasMultiplication = False
    wasDivision = False
    expectedNumber = True

    for token in parse_input_string_to_tokens(input_value):
        if token in "-+*/":
            if expectedNumber:
                raise CalculateException(f"Expected operator, got: {token}")

            operators.append(token)
            wasMultiplication = token == "*"
            wasDivision = token == "/"
            expectedNumber = True
        elif isdigit(token):
            if not expectedNumber:
                raise CalculateException(f"Expected number, got: {token}")

            value = float(token)
            if wasMultiplication:
                first = numbers.pop()
                operators.pop()

                numbers.append(first * value)
                wasMultiplication = False
            elif wasDivision:
                first = numbers.pop()
                operators.pop()

                numbers.append(first / value)
                wasDivision = False
            else:
                numbers.append(value)

            expectedNumber = False
        else:
            raise CalculateException(f"Unexpected token, got: {token}")

    while operators:
        operator = operators.pop()
        second = numbers.pop()
        first = numbers.pop()

        if operator == "-":
            numbers.append(first - second)
        elif operator == "+":
            numbers.append(first + second)

    return float(numbers[0])
