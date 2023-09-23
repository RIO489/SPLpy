from cmath import sqrt
from variables import defaultroundto
from variables import memory
from variables import results

#User class
class User:
    def __init__(self,name):
        self.name = name
        self.roundto = defaultroundto
        self.memory = memory

#Function that save result of calculation into result[] for repetative usage 
def writeIn(result):
    write = input('Do you wish to save the result? Y N: ')
    if(write == 'Y' or write == 'y'):
        results.append(round(result, defaultroundto)) 

#function that return number from result[]        
def useResult():
        for i in range (0, len(results)): 
            print(results[i])
            confirm = input('Do you want to use this number as num1? Y N: ')
            if(confirm == 'Y' or confirm == "y"):
                return results[i]

#function that save numbers,operators and result of calculation in history[]            
def save(num1,num2,operator,result):
    new_array = [num1,num2,operator,result]
    user.memory.append(new_array)

#main calculations:
name = ''
while(1):
    if(name == ''):
        name = input('Enter your name: ')
        user = User(name)
        setting = input('Do you wish to change user setting? Y N: ')
        if(setting == 'Y' or setting == "y"):
                user.roundto = int(input('How many number after dot should be visible? (1-9): '))

    if(len(results)):
        write = input('Do you with to use results? Y N: ')
        if(write == 'Y' or write == 'y'):
            num1=useResult()
        else:
            num1 = float(input('Enter a first number: '))
    else:
        num1 = float(input('Enter a first number: '))
    num2 = float(input('Enter a second number: '))
    operator = input('Enter a operator(+,-,*,/,^,√,%) : ')

    match operator:
        case('+'):
            result = num1+num2
            print(round(result,user.roundto))
            writeIn(result)
            save(num1,num2,operator,result)
        case('-'):
            result = num1 - num2
            print(round(result,user.roundto))
            writeIn(result)
            save(num1,num2,operator,result)
        case('*'):
            result = num1*num2
            print(round(result,user.roundto))
            writeIn(result)
            save(num1,num2,operator,result)
        case('/'):
            if(num2 == 0):
                print('You can`t divide by 0')
            else:
                result = num1/num2
                print(round(result,user.roundto))
                writeIn(result)
                save(num1,num2,operator,result)
        case('^'):
            result = pow(num1,num2)
            print(round(result,user.roundto))
            writeIn(result)
            save(num1,num2,operator,result)
        case('√'):
                count = 0
                multiplier = num2
                while(num1 >= num2):
                    num2 *= multiplier
                    count+=1
                result = num1/num2+count
                print(round(result,user.roundto))
                writeIn(result)
                save(num1,multiplier,operator,result)
        case('%'):
            if(num2 == 0):
                print('You can`t divide by 0')
            else:
                result = num1%num2
                print(round(result,user.roundto))
                writeIn(result)
                save(num1,num2,operator,result)
        case _:
            print('smth went wrong,please check your inputs')


#function that allow user to view their calculation history
    viewHistory = input('Do you want to see your history? Y N: ')
    if(viewHistory == 'Y' or viewHistory == "y"):
        for i in range (0, len(user.memory)): 
            print(user.memory[i])
            

    answer = input('Do you want to make another calculation? Y N: ')
    if(answer == 'N' or answer == "n"):
            exit()