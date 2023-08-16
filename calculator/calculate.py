from typing import Iterable
from .parsing import (
    Bracket,
    Operator,
    convert_infix_into_postfix_notation,
    parse_tokens,
    split_input_string_to_tokens,
)


class CalculateException(Exception):
    pass


def calculate_postfix_notation(tokens: Iterable[int | Operator | Bracket]) -> int:
    stack = []

    for token in tokens:
        if type(token) == Operator:
            parameters_list = [stack.pop() for _ in range(token.parameters_count)][::-1]
            stack.append(token.function(*parameters_list))
        else:
            stack.append(token)

    return stack.pop()


def calculate(input_value: str) -> int:
    if input_value == "":
        return 0

    return calculate_postfix_notation(
        convert_infix_into_postfix_notation(
            parse_tokens(split_input_string_to_tokens(input_value))
        )
    )
