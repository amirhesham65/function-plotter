from .tokens import TokenType
from .nodes import *

# The idea of a parser is to parse a given set of tokens into a corresponding tree structure
# in order to make it easier for the interpreter (next stage).
# So for example the expression '2+3' should be parsed into:
#         (AddNode)
#         /       \
# (NumberNode)  (NumberNode)


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()

    def raise_syntax_error(self):
        raise Exception("Invalid Syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    # Parsing a whole given set of tokens
    def parse(self):
        if self.current_token is None:
            return None

        result = self.expr()

        # current_token should be None after evaluating all tokens
        if self.current_token is not None:
            self.raise_syntax_error()

        return result

    # Search for the next expression e.g: '2+3' is a valid expression
    def expr(self):
        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())
        return result

    # Search for the next term e.g: '2*3' is a valid term
    def term(self):
        result = self.exp()

        while self.current_token is not None and \
                self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.exp())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.exp())
        return result

    # Exponent expression like x^3 has higher precedence than multiplication and division
    def exp(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type == TokenType.POWER:
            self.advance()
            result = PowerNode(result, self.factor())
        return result

    # Search for the next factor or unary operator
    def factor(self):
        token = self.current_token

        # Adding the precedence of the () parenthesis
        if token.type == TokenType.LEFT_PAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type != TokenType.RIGHT_PAREN:
                self.raise_syntax_error()
            self.advance()
            return result

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.X:
            self.advance()
            return XNode()
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        self.raise_syntax_error()
