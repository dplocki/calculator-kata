import re
from typing import Iterable, Union


def parse_input_string_to_tokens(
    input_value: str,
) -> Iterable[Union[int, str], None, None]:
    yield from filter(lambda token: token.strip() != "", re.split("(\W)", input_value))


def calculate(input_value: str) -> int:
    if input_value == "":
        return 0

    operator = "+"
    result = 0

    for token in parse_input_string_to_tokens(input_value):
        if token in "-+":
            operator = token
        else:
            if operator == "+":
                result += int(token)
            elif operator == "-":
                result -= int(token)

    return result
