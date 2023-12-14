""" Main file"""
from Data.data import color_mapping
from .Classes.generator import ASCIIArtGenerator
from .Classes.input import InputHandler

def main() -> None:
    """ Main method"""
    handler = InputHandler()
    user_language = handler.get_language(input("Enter language"))
    user_input = handler.get_user_input(input("Введіть слово або фразу для ASCII-арту: "))
    size = handler.get_art_size(input("Введіть ширину (1-100):"),input("Введіть висоту (1-100):"))
    width = size[0]
    height = size[1]
    alignment = handler.get_alignment(input("Виберіть вирівнювання тексту (left, center, right): "))
    color = color_mapping[handler.get_color(input("Оберіть колір @(чорний), #(сірий), *(білий)]:"))]
    ascii_art = ASCIIArtGenerator(user_input,color,width,height,alignment,user_language)

    ascii_art.generate_ascii_art()
    ascii_art.display_ascii_art()
    ascii_art.save_to_file()
    user_control = handler.get_answer(input('Чи бажаєте Ви продовжити? Y N: '))
    if(user_control in ['N','n','no']):
        exit()

if __name__ == '__main__':
    while 1:
        main()
