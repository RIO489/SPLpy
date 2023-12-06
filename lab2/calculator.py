from lab2.data import results
from lab2.exception import CalculationException, IncorrectOperatorException
from lab2.user import User

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