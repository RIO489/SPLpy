""" Main file"""
from Shared.calculator import Calculator
from Shared.user import User

def init_user():
    """ Initializing user"""
    user = User(input("Enter your name: "))
    if input('Do you wish to change roundto ? Y N :').lower == 'y':
        roundto = int(input('How many number after dot should be visible? (1-9): '))
        user.change_roundto(roundto)
    return user

#Firstly we need to enter username 
def main() ->None:
    """ Main method"""
    user = init_user()
    calculator = Calculator()
    while (2+2)!=5:
        calculator.calculations(user)
        if calculator.repeat() is False:
            break
        calculator.input()
        #calculator.useResult()
