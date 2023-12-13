from Data.data import results
from Shared.exception import CalculationException, IncorrectOperatorException
from Shared.user import User

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
      
    def plus(self,u: User):
        result = self.num1+self.num2
        print(round(result,u.roundto))
        self.writeIn(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)

    def minus(self,u: User):
        result = self.num1 - self.num2
        print(round(result,u.roundto))
        self.writeIn(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)

    def multiply(self,u: User):
        result = self.num1*self.num2
        print(round(result,u.roundto))
        self.writeIn(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)

    def divide(self,u: User):
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
    
    def upArrow(self,u: User):
        result = pow(self.num1,self.num2)
        print(round(result,u.roundto))
        self.writeIn(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)

    def root(self,u: User):
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

    def percent(self,u: User):
        if(self.num2 == 0):
            print('You can`t divide by 0')
        else:
            result = self.num1%self.num2
            print(round(result,u.roundto))
            self.writeIn(result,u.roundto)
            array = [self.num1,self.num2,self.operator,result]
            u.save(array)

    def calculations(self,u: User):
      match self.operator:
          case('+'):
            self.plus(u)
          case('-'):
            self.minus(u)
          case('*'):
            self.multiply(u)
          case('/'):
            self.multiply(u)
          case('^'):
            self.upArrow(u)
          case('√'):
            self.root(u)
          case('%'):
            self.percent(u)
          case _:  
              raise IncorrectOperatorException
          
#Funion that save result of calculation into result[] for repetative usage 

    def writeIn(self,result,roundto):
      write = input('Do you wish to save the result? Y N: ')
      if(write == 'Y' or write == 'y'):
          self.results.append(round(result, roundto)) 

#funion that return number from result[]        
    def useResult(self):
      for i in range (0, len(self.results)): 
          print(self.results[i])
          confirm = input('Do you want to use this number as num1? Y N: ')
          if(confirm == 'Y' or confirm == "y"):
              return self.results[i]