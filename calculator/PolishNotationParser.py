class PolishNotationParser:
    def parse(self, value):
        if value == "":
            return []

        tokens = value.split()
        if len(tokens) == 1:
            return [int(tokens[0])]

        return [tokens[1], int(tokens[0]), int(tokens[2])]
