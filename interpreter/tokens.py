from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LEFT_PAREN = 5
    RIGHT_PAREN = 6
    POWER = 7
    X = 8


class Token:
    def __init__(self, token_type: TokenType, value: any = None):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")