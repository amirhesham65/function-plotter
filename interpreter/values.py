# Type of returned values from expressions
# since it's an arithmetic interpreter we only return a number
class Number:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value}"
