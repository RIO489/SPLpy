from cmath import sqrt
from exception import CalculationException, IncorrectOperatorException
from data import results
from user import User

class Calculator:
     def __init__(self):
          self.Input()
          self.results = results

     def Input(self):
       self.num1 = float(input('Enter a first number: '))
       self.num2 = float(input('Enter a second number: '))
       self.operator = input('Enter a operator(+,-,*,/,^,√,%) : ')
        
     def repeat(self):
        answer = input('Do you want to make another calculation? Y N: ')
        if(answer == 'N' or answer == "n"):
            return False
            
     def calculations(self,u: User):
        match self.operator:
            case('+'):
                result = self.num1+self.num2
                print(round(result,u.roundto))
                self.writeIn(result,u.roundto)
                array = [self.num1,self.num2,self.operator,result]
                u.save(array)
            case('-'):
                result = self.num1 - self.num2
                print(round(result,u.roundto))
                self.writeIn(result,u.roundto)
                array = [self.num1,self.num2,self.operator,result]
                u.save(array)
            case('*'):
                result = self.num1*self.num2
                print(round(result,u.roundto))
                self.writeIn(result,u.roundto)
                array = [self.num1,self.num2,self.operator,result]
                u.save(array)
            case('/'):
                try:
                    if(self.num2 == 0):
                        raise CalculationException(self.num2)
                    else:
                        result = self.num1/self.num2
                        print(round(result,u.roundto))
                        self.writeIn(result, u.roundto)
                        array = [self.num1,self.num2,self.operator,result]
                        u.save(array)
                except CalculationException as e:
                    print("Exception occurred:", str(e))
            case('^'):
                result = pow(self.num1,self.num2)
                print(round(result,u.roundto))
                self.writeIn(result,u.roundto)
                array = [self.num1,self.num2,self.operator,result]
                u.save(array)
            case('√'):
                count = 0
                multiplier = self.num2
                while(self.num1 >= self.num2):
                    self.num2 *= multiplier
                    count+=1
                result = self.num1/self.num2+count
                print(round(result,u.roundto))
                self.writeIn(result,u.roundto)
                array = [self.num1,self.num2,self.operator,result]
                u.save(array)
            case('%'):
                if(self.num2 == 0):
                    print('You can`t divide by 0')
                else:
                    result = self.num1%self.num2
                    print(round(result,u.roundto))
                    self.writeIn(result,u.roundto)
                    array = [self.num1,self.num2,self.operator,result]
                    u.save(array)
            case _:  
                raise IncorrectOperatorException
            
#Function that save result of calculation into result[] for repetative usage 

     def writeIn(self,result,roundto):
        write = input('Do you wish to save the result? Y N: ')
        if(write == 'Y' or write == 'y'):
            self.results.append(round(result, roundto)) 

#function that return number from result[]        
     def useResult(self):
        for i in range (0, len(self.results)): 
            print(self.results[i])
            confirm = input('Do you want to use this number as num1? Y N: ')
            if(confirm == 'Y' or confirm == "y"):
                return self.results[i]

#main calculations:



#     if name == '':
#         name = input('Enter your name: ')
#         user = User(name)
#         setting = input('Do you wish to change user setting? Y N: ')
#         if(setting == 'Y' or setting == "y"):
#                 user.roundto = int(input('How many number after dot should be visible? (1-9): '))

#     if len(results):
#         write = input('Do you with to use results? Y N: ')
#         if write == 'Y' or write == 'y':
#             num1=useResult()
#         else:
#             num1 = float(input('Enter a first number: '))
#     else:
#         num1 = float(input('Enter a first number: '))
#     num2 = float(input('Enter a second number: '))
#     operator = input('Enter a operator(+,-,*,/,^,√,%) : ')

#     match operator:
#         case('+'):
#             result = num1+num2
#             print(round(result,user.roundto))
#             writeIn(result)
#             save(num1,num2,operator,result)
#         case('-'):
#             result = num1 - num2
#             print(round(result,user.roundto))
#             writeIn(result)
#             save(num1,num2,operator,result)
#         case('*'):
#             result = num1*num2
#             print(round(result,user.roundto))
#             writeIn(result)
#             save(num1,num2,operator,result)
#         case('/'):
#             if(num2 == 0):
#                 raise CalculationException()
#                 print('You can`t divide by 0')
#             else:
#                 result = num1/num2
#                 print(round(result,user.roundto))
#                 writeIn(result)
#                 save(num1,num2,operator,result)
#         case('^'):
#             result = pow(num1,num2)
#             print(round(result,user.roundto))
#             writeIn(result)
#             save(num1,num2,operator,result)
#         case('√'):
#                 count = 0
#                 multiplier = num2
#                 while(num1 >= num2):
#                     num2 *= multiplier
#                     count+=1
#                 result = num1/num2+count
#                 print(round(result,user.roundto))
#                 writeIn(result)
#                 save(num1,multiplier,operator,result)
#         case('%'):
#             if(num2 == 0):
#                 print('You can`t divide by 0')
#             else:
#                 result = num1%num2
#                 print(round(result,user.roundto))
#                 writeIn(result)
#                 save(num1,num2,operator,result)
#         case _:
#             print('smth went wrong,please check your inputs')


# #function that allow user to view their calculation history
#     viewHistory = input('Do you want to see your history? Y N: ')
#     if viewHistory == 'Y' or viewHistory == "y":
#         for i in range (0, len(user.memory)): 
#             print(user.memory[i])
            

#     answer = input('Do you want to make another calculation? Y N: ')
#     if answer == 'N' or answer == "n":
#             exit()