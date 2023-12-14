""" Calculator"""
import logging
from Data.data import results
from Shared.exception import CalculationException, IncorrectOperatorException
from Shared.user import User

class Calculator:
    """ Calculator class"""
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator =0
        self.results = results

    def input(self):
        """ Input values"""
        self.num1 = float(input('Enter a first number: '))
        self.num2 = float(input('Enter a second number: '))
        self.operator = input('Enter a operator(+,-,*,/,^,√,%) : ')

    def repeat(self):
        """ Repeat proccess"""
        answer = input('Do you want to make another calculation? Y N: ')
        if(answer == 'N' or answer == "n"):
            return False

    def plus(self,u: User):
        """ Plus"""
        result = self.num1+self.num2
        print(round(result,u.roundto))
        self.write_in(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)
        logging.info("Calculator is made a calculation: %s",array)

    def minus(self,u: User):
        """ minus """
        result = self.num1 - self.num2
        print(round(result,u.roundto))
        self.write_in(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)
        logging.info("Calculator is made a calculation: %s",array)

    def multiply(self,u: User):
        """multiply """
        result = self.num1*self.num2
        print(round(result,u.roundto))
        self.write_in(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)
        logging.info("Calculator is made a calculation: %s",array)

    def divide(self,u: User):
        """ dividing"""
        try:
            if self.num2 == 0:
                raise CalculationException(self.num2)
            else:
                result = self.num1/self.num2
                print(round(result,u.roundto))
                self.write_in(result, u.roundto)
                array = [self.num1,self.num2,self.operator,result]
                u.save(array)
                logging.info("Calculator is made a calculation: %s",array)
        except CalculationException as e:
            print("Exception occurred:", str(e))

    def power(self,u: User):
        """ pow"""
        result = pow(self.num1,self.num2)
        print(round(result,u.roundto))
        self.write_in(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)
        logging.info("Calculator is made a calculation: %s",array)

    def root(self,u: User):
        """ √"""
        count = 0
        multiplier = self.num2
        while self.num1 >= self.num2:
            self.num2 *= multiplier
            count+=1
        result = self.num1/self.num2+count
        print(round(result,u.roundto))
        self.write_in(result,u.roundto)
        array = [self.num1,self.num2,self.operator,result]
        u.save(array)
        logging.info("Calculator is made a calculation: %s",array)

    def percent(self,u: User):
        """ % """
        if self.num2 == 0:
            print('You can`t divide by 0')
        else:
            result = self.num1%self.num2
            print(round(result,u.roundto))
            self.write_in(result,u.roundto)
            array = [self.num1,self.num2,self.operator,result]
            u.save(array)
            logging.info("Calculator is made a calculation: %s",array)

    def calculations(self,u: User):
        """ Main calculations"""
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
                self.power(u)
            case('√'):
                self.root(u)
            case('%'):
                self.percent(u)
            case _:
                raise IncorrectOperatorException

#Funion that save result of calculation into result[] for repetative usage

    def write_in(self,result,roundto):
        """ save file"""
        write = input('Do you wish to save the result? Y N: ')
        if(write == 'Y' or write == 'y'):
            self.results.append(round(result, roundto))

#funion that return number from result[]
    def use_result(self):
        """ use results"""
        for value in enumerate(self.results):
            print(value)
            confirm = input('Do you want to use this number as num1? Y/N: ')
            if confirm.lower() in ('y', 'yes'):
                return value

    def test_plus(self,num1,num2):
        """ test plus"""
        return int(num1) + int(num2)

    def test_multiply(self,num1,num2):
        """ test plus"""
        return float(num1) * float(num2)
    