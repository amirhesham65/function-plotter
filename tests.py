import unittest
from interpreter.lexer import Lexer
from interpreter.parser_ import Parser
from interpreter.interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_arithmetic(self):
        """
        Test that the interpreter parser can evaluate an arithmetic expression
        """
        lexer = Lexer("2 + 2 * (5 - 3) / 4")
        tokens = lexer.generate_tokens()
        p = Parser(tokens)
        tree = p.parse()
        self.assertEqual(Interpreter().visit(tree).value, 3)

    def test_function_expression(self):
        lexer = Lexer("x^3 + 44")
        tokens = lexer.generate_tokens()
        p = Parser(tokens)
        tree = p.parse()
        self.assertEqual(Interpreter(x=5).visit(tree).value, 169)


if __name__ == '__main__':
    unittest.main()
