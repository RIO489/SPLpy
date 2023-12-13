from cmath import sqrt
from Data.data import results, count


#Function that save result of calculation into result[] for repetative usage 
def writeIn(result,user):
    write = input('Do you wish to save the result? Y N: ')
    if(write == 'Y' or write == 'y'):
        results.append(round(result, user.roundto)) 

#function that return number from result[]        
def useResult():
        for i in range (0, len(results)): 
            print(results[i])
            confirm = input('Do you want to use this number as num1? Y N: ')
            if(confirm == 'Y' or confirm == "y"):
                return results[i]

#function that save numbers,operators and result of calculation in history[]            
def save(num1,num2,operator,result,user):
    new_array = [num1,num2,operator,result]
    user.memory.append(new_array)


def plus(num1,num2,operator,user):
    result = num1+num2
    print(round(result,user.roundto))
    writeIn(result,user)
    save(num1,num2,operator,result,user)

def minus(num1,num2,operator,user):
    result = num1 - num2
    print(round(result,user.roundto))
    writeIn(result,user)
    save(num1,num2,operator,result,user)
  
def multiply(num1,num2,operator,user):
    result = num1*num2
    print(round(result,user.roundto))
    writeIn(result,user)
    save(num1,num2,operator,result,user)
  
def divide(num1,num2,operator,user):
    if(num2 == 0):
        print('You can`t divide by 0')
    else:
        result = num1/num2
        print(round(result,user.roundto))
        writeIn(result,user)
        save(num1,num2,operator,result,user)

def upArrow(num1,num2,operator,user):
    result = pow(num1,num2)
    print(round(result,user.roundto))
    writeIn(result,user)
    save(num1,num2,operator,result,user)

def root(num1,num2,operator,user):
    global count
    multiplier = num2
    while(num1 >= num2):
         num2 *= multiplier
         count+=1
    result = num1/num2+count
    print(round(result,user.roundto))
    writeIn(result,user)
    save(num1,multiplier,operator,result,user)
    count = 0

def percent(num1,num2,operator,user):
    if(num2 == 0):
       print('You can`t divide by 0')
    else:
       result = num1%num2
       print(round(result,user.roundto))
       writeIn(result,user)
       save(num1,num2,operator,result,user)