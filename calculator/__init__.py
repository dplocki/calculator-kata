from functools import reduce
import re


def calculate(value: str):
    if value == "":
        return 0

    operator = "+"
    result = 0

    for token in filter(lambda token: token.strip() != '', re.split('(\W)', value)):
        if token in "-+":
            operator = token
        else:
            if operator == "+":
                result += int(token)
            elif operator == "-":
                result -= int(token)

    return result
