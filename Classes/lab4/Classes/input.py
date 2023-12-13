from Shared.exception import IncorrectArgumentException 
from Data.languages import *

class InputHandler:
    def get_user_input():
        input_value = input("Введіть слово або фразу для ASCII-арту: ")
        if input_value.isalpha():
            return input_value
        else:
            raise IncorrectArgumentException("Input must contain only alphabetic characters.")
        


    def get_art_size():
        input_width = input("Введіть ширину ASCII-арту (1-100): ")
        input_height = input("Введіть висоту ASCII-арту (1-100): ")

        if input_width.isdigit() and input_height.isdigit():
            width = int(input_width)
            height = int(input_height)
        else:
            raise IncorrectArgumentException()
        
        result = [width, height]
        return result

    def get_alignment():
        input_value = input("Виберіть вирівнювання тексту (left, center, right): ").lower()
        if (input_value.isalpha() and input_value in ['left', 'center', 'right']):
            return input_value
        else:
            raise IncorrectArgumentException()
    
    def get_color():
        input_value = input("Введіть символи кольорів для ASCII-арту ['@'(чорний), '#'(сірий), '*'(білий)]: ")
        if input_value in ['@', '#', '*']:
            return input_value
        else:
            raise IncorrectArgumentException()
        

    def get_language():
        input_value = input("Яку мови використати для генерації ASCII арту [eng,ukr]: ")
        if input_value == 'eng' or input_value == 'ukr':
            if(input_value =='eng'):
                return english_font
            else:
                return ukraine_font
        else:
            raise IncorrectArgumentException()
        
    def get_answer():
       user_control = input('Чи бажаєте Ви продовжити? Y N: ')
       if user_control in ['Y', 'y', 'yes','N','n','no']:
           return user_control
       else:
           raise IncorrectArgumentException()


