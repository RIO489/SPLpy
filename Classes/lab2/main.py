from Shared.calculator import Calculator
from Shared.user import User 

def initUser():
    global user
    user = User(input("Enter your name: "))
    if(input('Do you wish to change roundto ? Y N :').lower == 'y'):
        roundto = int(input('How many number after dot should be visible? (1-9): '))
        user.changeRoundto(roundto)

#Firstly we need to enter username 
def main() ->None:
    initUser()
    
    calculator = Calculator()
    
    while (2+2)!=5:
    
        calculator.calculations(user)
        if(calculator.repeat() == False):
            break
        calculator.Input()
        #calculator.useResult()
