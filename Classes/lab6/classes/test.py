""" Test"""
import unittest
from Shared.calculator import Calculator
class TestCalculator(unittest.TestCase):
    """ Test for unittesting calculator"""

    def test_add(self):
        """Add test """
        calculator = Calculator()
        num1 = 2.
        num2 = 2.
        result = calculator.test_plus(num1,num2)
        self.assertEqual(result, 4)

    def test_multiply(self):
        """ Mulitply test"""
        calculator = Calculator()
        num1 = 2.
        num2 = 2.
        result = calculator.test_multiply(num1,num2)
        self.assertEqual(result, 4)
