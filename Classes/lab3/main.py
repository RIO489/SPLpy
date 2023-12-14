""" Main file"""
import sys
import logging
import art
from termcolor import colored
from Data.data import USER_FONT,colors,memory

def print_art(user_art):
    """Print user art"""
    sys.stdout.write(user_art)

def change_chr(text,replacement_dict):
    """Change user character"""
    for old_char, new_char in replacement_dict.items():
        text = text.replace(old_char, new_char)
    return text

def draw_art(text,font,user_char):
    """Draw user art"""
    return art.text2art(text,font,user_char)

def different_chr():
    """Use different character"""
    return {'#': input("Enter the characters you want to use for ASCII art: ")[0]}

def enter_text():
    """Enter user text to transform into art"""
    if input("Do you want use different chr? Y N :") == 'Y' or 'y' :
        replacement_dict = different_chr()
    text = input("Write text: ")
    user_art = draw_art(text,USER_FONT,replacement_dict)
    if replacement_dict is not None:
        for old_char, new_char in replacement_dict.items():
            user_art = user_art.replace(old_char, new_char)
    print(user_art)
    save_art(user_art)

def save_art(user_art):
    """Save art"""
    if(input("Save the art? Y N :").strip().lower() == "Y" or "y"):
        filename = "Data/test.txt"
        art.tsave(user_art,USER_FONT,filename=filename)
        logging.info("Art is saved")

def print_fonts():
    """Print all fonts in system"""
    art.font_list()
    new_font = input("Choose font: ")
    print(art.text2art(text="test",font=new_font))

def main() -> None:
    """Main method"""
    while 1:
        print("1) Enter text")
        print("2) Change font")
        print("3) Print arts")
        print("4) Change color")
        print("5) Quit")

        choice = input("Enter choice: ")

        match(choice):
            case("1"):
                enter_text()

            case("2"):
                print_fonts()

            case("3"):
                print(memory)

            case("4"):
                for color in colors:
                    print_art(colored(art.text2art(text="test",font=USER_FONT),color))

            case("5"):
                break
