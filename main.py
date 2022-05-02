from interpreter.lexer import Lexer
from interpreter.parser_ import Parser

if __name__ == '__main__':
    while True:
        expression = input("calc > ")
        lexer = Lexer(expression)
        tokens = lexer.generate_tokens()
        # print(list(tokens))
        p = Parser(tokens)
        tree = p.parse()
        print(tree)

