import operator
from functools import reduce


def calculate(value):
    if value == "":
        return 0

    if "+" in value:
        tokens = value.split("+")
        return sum(map(int, tokens))

    if "-" in value:
        tokens = value.split("-")
        return reduce(operator.sub, map(int, tokens))

    return int(value)
