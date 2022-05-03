import unittest
from gui import GUIApp
from interpreter.arithmetic_interpreter import ArithmeticInterpreter


class TestGUI(unittest.TestCase):
    def test_expression_evaluation_interval(self):
        """
         Test that app can evaluate an expression on an interval and produce an interval
        """
        self.assertEqual(GUIApp.evaluate_function_string("x*2", 0.0, 3.0), ([0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]))


class TestInterpreter(unittest.TestCase):
    def test_addition(self):
        """
        Test that the interpreter parser can evaluate an addition expression
        """
        self.assertEqual(ArithmeticInterpreter.evaluate("6+2"), 8)

    def test_subtraction(self):
        """
        Test that the interpreter parser can evaluate a subtraction expression
        """
        self.assertEqual(ArithmeticInterpreter.evaluate("6-2"), 4)

    def test_multiplication(self):
        """
        Test that the interpreter parser can evaluate a multiplication expression
        """
        self.assertEqual(ArithmeticInterpreter.evaluate("6*2"), 12)

    def test_division(self):
        """
        Test that the interpreter parser can evaluate a division expression
        """
        self.assertEqual(ArithmeticInterpreter.evaluate("6/2"), 3)

    def test_power(self):
        """
        Test that the interpreter parser can evaluate a power expression
        """
        self.assertEqual(ArithmeticInterpreter.evaluate("6^2"), 36)

    def test_calc_with_x(self):
        """
        Test that the interpreter parser can evaluate an expression with a variable x value
        """
        self.assertEqual(ArithmeticInterpreter.evaluate("5*x^3 + 2*x", x_value=5), 635)


if __name__ == '__main__':
    unittest.main()
