from interpreter.lexer import Lexer

if __name__ == '__main__':
    while True:
        expression = input("calc > ")
        lexer = Lexer(expression)
        tokens = lexer.generate_tokens()
        print(list(tokens))

