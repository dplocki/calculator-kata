import random


def generate_int():
    return random.randrange(0, 99999)


def generate_operation():
    return random.choice(["-", "+", "*", "/"])
