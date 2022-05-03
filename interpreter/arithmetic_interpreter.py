from interpreter.lexer import Lexer
from interpreter.parser_ import Parser
from interpreter.interpreter import Interpreter


class ArithmeticInterpreter:

    @staticmethod
    def evaluate(expression: str, x_value: float = 0) -> float:
        lexer = Lexer(expression)
        tokens = lexer.generate_tokens()
        p = Parser(tokens)
        tree = p.parse()
        return Interpreter(x_value).visit(tree).value
    