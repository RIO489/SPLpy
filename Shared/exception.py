"""Calculator exception """
class CalculationException(Exception):
    """ Exception class for calculator"""
    def __init__(self, num2):
        self.num2 = num2
        super().__init__()


class IncorrectOperatorException(Exception):
    """ Incorrect Operator"""
    def __init__(self, message="Invalid operator"):
        self.message = message
        super().__init__(message)

class IncorrectArgumentException(Exception):
    """ Incorrect argument"""
    def __init__(self, num2):
        self.num2 = num2
        super().__init__()
