from interpreter.lexer import Lexer
from interpreter.parser_ import Parser
from interpreter.interpreter import Interpreter


if __name__ == '__main__':
    while True:
        try:
            expression = input("calc > ")
            lexer = Lexer(expression)
            tokens = lexer.generate_tokens()
            p = Parser(tokens)
            tree = p.parse()
            if not tree:
                continue
            interpreter = Interpreter(3)
            value = interpreter.visit(tree)
            print(value)
        except Exception as e:
            print(e)

