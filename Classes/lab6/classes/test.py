import unittest
from Shared.calculator import Calculator
from Shared.user import User
class TestCalculator(unittest.TestCase):
    #def test_input(self):
    #    self.assertIsInstance(float(5),float)
    #    with self.assertRaises(ValueError):
    #        self.assertIsInstance(int(5), float)

    def test_add(self):
        user = User("test")
        calculator = Calculator()
        calculator.num1 = 1.0
        calculator.num2 = 2.0
        calculator.operator = '+'
        calculator.plus(user)
        result = calculator.results[0]
        self.assertEqual(result, 3)

    def test_multiply(self):
        user = User("test")
        calculator = Calculator()
        calculator.num1 = 1.0
        calculator.num2 = 2.0
        calculator.operator = '*'
        calculator.multiply(user)
        result = calculator.results[1]
        self.assertEqual(result, 2)


        
  #  # Завдання 1: Тестування Додавання
  #  def test_add(self):
  #      self.assertEqual(Calculator.add(1, 2), 3)
  #      self.assertEqual(Calculator.add(-1, -2), -3)
  #      self.assertEqual(Calculator.add(-1, 1), 0)
#
  #  # Завдання 2: Тестування Віднімання
  #  def test_subtract(self):
  #      self.assertEqual(Calculator.subtract(5, 3), 2)
  #      self.assertEqual(Calculator.subtract(-1, -2), 1)
  #      self.assertEqual(Calculator.subtract(-1, 1), -2)
  #      self.assertEqual(Calculator.subtract(1, -1), 2)
#
  #  # Завдання 3: Тестування Множення
  #  def test_multiply(self):
  #      self.assertEqual(Calculator.multiply(3, 2), 6)
  #      self.assertEqual(Calculator.multiply(-1, -2), 2)
  #      self.assertEqual(Calculator.multiply(-1, 2), -2)
  #      self.assertEqual(Calculator.multiply(0, 100), 0)
#
  #  # Завдання 4: Тестування Ділення
  #  def test_divide(self):
  #      self.assertEqual(Calculator.divide(6, 2), 3)
  #      self.assertEqual(Calculator.divide(-4, -2), 2)
  #      self.assertEqual(Calculator.divide(-4, 2), -2)
  #      with self.assertRaises(ValueError):
  #          Calculator.divide(5, 0)
#
  #  # Завдання 5: Тестування Обробки Помилок
  #  def test_divide_errors(self):
  #      with self.assertRaises(ValueError):
  #          Calculator.divide(10, 0)