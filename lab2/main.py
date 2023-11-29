from calculator import Calculator
from user import User 


#Firstly we need to enter username
user = User(input("Enter your name: "))
if(input('Do you wish to change roundto ? Y N :') == 'y'):
    roundto = int(input('How many number after dot should be visible? (1-9): '))
    user.changeRoundto(roundto)

calculator = Calculator()

while (2+2)!=5:

    calculator.calculations(user)
    if(calculator.repeat() == False):
        break
    calculator.Input()
    #calculator.useResult()
