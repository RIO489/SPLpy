""" Calculator"""
from Data.data import results, COUNT

# Function that saves the result of a calculation into the 'results' list for repetitive usage.
def write_in(result, user):
    """
    This function prompts the user to save the result and appends it 
    to the 'results' list if confirmed.

    Args:
        result (float): The result of a calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    write = input('Do you wish to save the result? Y N: ')
    if write.lower() == 'y':
        results.append(round(result, user.roundto))

# Function that returns a number from the 'results' list.
def use_result():
    """
    This function allows the user to select a saved result and returns it for further calculations.

    Returns:
        float: The selected result from the 'results' list.
    """
    for result in enumerate(results):
        print(result)
        confirm = input('Do you want to use this number as num1? Y/N: ')
        if confirm.lower() == 'y':
            return result

# Function that saves numbers, operators, and the result of a calculation in the 'user.memory' list.
def save(num1, num2, operator, result, user):
    """
    This function creates a new record of a calculation and appends it to 
    the user's calculation history.

    Args:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operator (str): The operator used for the calculation.
        result (float): The result of the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    new_record = [num1, num2, operator, result]
    user.memory.append(new_record)

#The following functions perform basic arithmetic operations (addition, subtraction, multiplication,
#division,exponentiation, root calculation, and percentage) and
# utilize the write_in() and save() functions to manage results.

def plus(num1, num2, operator, user):
    """
    Perform addition, print the result, and save the result in the user's history.

    Args:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    result = num1 + num2
    print(round(result, user.roundto))
    write_in(result, user)
    save(num1, num2, operator, result, user)
def minus(num1,num2,operator,user):
    """
    Calculate the minus of 'num1' with respect to 'num2' and save the result.

    Args:
        num1 (float): The number for which the percentage is calculated.
        num2 (float): The reference number.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    result = num1 - num2
    print(round(result,user.roundto))
    write_in(result,user)
    save(num1,num2,operator,result,user)
def multiply(num1,num2,operator,user):
    """
    Calculate the multiply of 'num1' with respect to 'num2' and save the result.

    Args:
        num1 (float): The number for which the percentage is calculated.
        num2 (float): The reference number.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    result = num1*num2
    print(round(result,user.roundto))
    write_in(result,user)
    save(num1,num2,operator,result,user)
def divide(num1,num2,operator,user):
    """
    Calculate the dividing of 'num1' with respect to 'num2' and save the result.

    Args:
        num1 (float): The number for which the percentage is calculated.
        num2 (float): The reference number.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    if num2 == 0:
        print('You can`t divide by 0')
    else:
        result = num1/num2
        print(round(result,user.roundto))
        write_in(result,user)
        save(num1,num2,operator,result,user)

def up_arrow(num1,num2,operator,user):
    """
    Calculate the pow of 'num1' with respect to 'num2' and save the result.

    Args:
        num1 (float): The number for which the percentage is calculated.
        num2 (float): The reference number.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    result = pow(num1,num2)
    print(round(result,user.roundto))
    write_in(result,user)
    save(num1,num2,operator,result,user)

def root(num1,num2,operator,user):
    """
    Calculate the root of 'num1' with respect to 'num2' and save the result.

    Args:
        num1 (float): The number for which the percentage is calculated.
        num2 (float): The reference number.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    global COUNT
    multiplier = num2
    while num1 >= num2:
        num2 *= multiplier
        COUNT+=1
    result = num1/num2+COUNT
    print(round(result,user.roundto))
    write_in(result,user)
    save(num1,multiplier,operator,result,user)
    COUNT = 0

def percent(num1,num2,operator,user):
    """
    Calculate the percentage of 'num1' with respect to 'num2' and save the result.

    Args:
        num1 (float): The number for which the percentage is calculated.
        num2 (float): The reference number.
        operator (str): The operator used for the calculation.
        user (User): An object containing user-specific settings.

    Returns:
        None
    """
    if num2 != 0:
        result = num1%num2
        print(round(result,user.roundto))
        write_in(result,user)
        save(num1,num2,operator,result,user)
    else:
        print('You can`t divide by 0')
