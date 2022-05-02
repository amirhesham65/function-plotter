from .tokens import Token, TokenType


class Lexer:
    def __init__(self, text: str):
        self.text = iter(text)
        self.current_char: str = None
        self.advance()

    def advance(self):
        # Traverse over the text iterator (one by one)
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        # loop over the text and parse its sections into tokens until reach the end
        while self.current_char is not None:
            # skip any whitespace
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit() or self.current_char == ".":
                yield self.generate_number()
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LEFT_PAREN)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RIGHT_PAREN)
            else:
                raise Exception(f"Invalid Syntax '{self.current_char}'")

    def generate_number(self):
        # Loop over each digit in a number as string
        number_str_builder = self.current_char
        self.advance()

        # Track the number of decimal place (e.g: '3.14.' should raise an error)
        decimal_points_count = 0

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == "."):
            if self.current_char == ".":
                decimal_points_count += 1
                if decimal_points_count > 1:
                    raise Exception(f"For a number expected 1 or 0 decimal places but given {decimal_points_count}")

            number_str_builder += self.current_char
            self.advance()

            if number_str_builder.startswith("."):
                # .14 -> 0.14
                number_str_builder = "0" + number_str_builder
            if number_str_builder.endswith("."):
                # 14. -> 14.0
                number_str_builder += "0"

        return Token(TokenType.NUMBER, float(number_str_builder))
