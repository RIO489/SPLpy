from Data.data import results , user_is_registered
from Shared.user import User
from .calculator import *

def register_user():
    """Mehtod for registering user"""
    name = input('Enter your name: ')
    newUser = User(name)
    return newUser


def changeUserSettings(user):
    if(input('Do you wish to change user setting? Y N: ').lower() == "y"):
        newRoundTo= int(input('How many number after dot should be visible? (1-9): '))
        user.changeRoundto(newRoundTo)

def useSavedresult():
    savedResult = None
    if(len(results)):
        if(input('Do you with to use results? Y N: ').lower()  == 'y'):
            savedResult = useResult()
    inputAll(savedResult)


def inputAll(number=None):
    global num1, num2, operator
    if number is None:
        num1 = float(input('Enter a first number: '))
    else:
        num1 = float(number)

    num2 = float(input('Enter a second number: '))
    operator = input('Enter an operator (+, -, *, /, ^, √, %): ')


#function that allow user to view their calculation history

def viewHistory(user):
    if(input('Do you want to see your history? Y N: ').lower() == "y"):
        user.history()
        
def repeat():
    if(input('Do you want to make another calculation? Y N: ').lower() == 'N' or "n"):
        exit()


def main() -> None:
    global user_is_registered, user
    if(user_is_registered == False):
        user = register_user()
        user_is_registered = True

    useSavedresult()

    match operator:
        case('+'):
            plus(num1,num2,operator,user)
        case('-'):
            minus(num1,num2,operator,user)
        case('*'):
            multiply(num1,num2,operator,user)
        case('/'):
            divide(num1,num2,operator,user)
        case('^'):
            upArrow(num1,num2,operator,user)
        case('√'):
            root(num1,num2,operator,user)
        case('%'):
            percent(num1,num2,operator,user)
        case _:
            print('smth went wrong,please check your inputs')

    viewHistory(user)
    repeat()
           
if __name__ == "__main__":
    while(1):
        main()