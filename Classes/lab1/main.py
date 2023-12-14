""" Main file"""
import logging
from Data.data import results , USER_IS_REGISTERED
from Shared.user import User
from .calculator import plus,minus,multiply,divide,percent,root,up_arrow,use_result


def register_user():
    """Mehtod for registering user"""
    name =  input('Enter your name: ')
    new_user = User(name)
    logging.info('User is registered: %s',name)
    return new_user


def change_user_settings(user_instance):
    """Mehtod for changing user settings"""
    if  input('Do you wish to change user setting? Y N: ').lower() == "y":
        new_round_to= int (input('How many number after dot should be visible? (1-9): '))
        user_instance.changeRoundto(new_round_to)
        logging.info('User roundTo variable is change to %s', new_round_to)

def use_saved_result():
    """Mehtod for using saved result"""
    saved_result = None
    if results:
        saved_result = use_result()
        logging.info('One of last results is being used %s ',saved_result)
        return saved_result


#def  input_all(number=None):
#    """Mehtod for inputing values"""
#   # global first_number, num2, operator
#    if number is None:
#        first_number = float (input('Enter a first number: '))
#    else:
#        first_number = float(number)
#
#    num2 = float (input('Enter a second number: '))
#    operator =  input('Enter an operator (+, -, *, /, ^, √, %): ')
#    logging.info('User entered numbers:  %s + %s and operator  %s ',first_number,num2,operator)


#function that allow user to view their calculation history

def view_history(user):
    """Mehtod for viewing user history """
    if input('Do you want to see your history? Y N: ').lower() == "y":
        user.history()
        logging.info("History is being viewed")

def repeat():
    """Mehtod for repeting whole proccess"""
    if input('Do you want to make another calculation? Y N: ').lower() == 'N' or "n":
        logging.warning("Program is closing!")
        exit()


def main() -> None:
    """Main menthod"""
    global USER_IS_REGISTERED
    if USER_IS_REGISTERED is False:
        user = register_user()
        USER_IS_REGISTERED = True

    if  input('Do you with to use results? Y N: '.lower()  == 'y'):
        first_number = use_saved_result()
    else:
        first_number = float (input('Enter a first number: '))

    num2 = float (input('Enter a second number: '))
    operator =  input('Enter an operator (+, -, *, /, ^, √, %): ')
    logging.info('User entered numbers:  %s + %s and operator  %s ',first_number,num2,operator)

    match operator:
        case('+'):
            plus(first_number,num2,operator,user)
        case('-'):
            minus(first_number,num2,operator,user)
        case('*'):
            multiply(first_number,num2,operator,user)
        case('/'):
            divide(first_number,num2,operator,user)
        case('^'):
            up_arrow(first_number,num2,operator,user)
        case('√'):
            root(first_number,num2,operator,user)
        case('%'):
            percent(first_number,num2,operator,user)
        case _:
            print('smth went wrong,please check your  inputs')

    view_history(user)
    repeat()
if __name__ == "__main__":
    while 1:
        main()
