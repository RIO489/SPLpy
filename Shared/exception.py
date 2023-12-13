class CalculationException(Exception):
    def __init__(self, num2):
        self.num2 = num2
        super().__init__()


class IncorrectOperatorException(Exception):
    def __init__(self, message="Invalid operator"):
        self.message = message
        super().__init__(message)

class IncorrectArgumentException(Exception):
     def __init__(self, num2):
        self.num2 = num2
        super().__init__()
