import art
import sys
from termcolor import colored
from lab3.data import *

def save_art(art):
    memory.append(art)

def printArt(art):
    sys.stdout.write(art)

def changeChr(text,replacement_dict):
    for old_char, new_char in replacement_dict.items():
        text = text.replace(old_char, new_char)
    return text

def draw_art(text,font,char):
        return art.text2art(text,font)


def main() -> None:
    while(1):
        print("1) Enter text")
        print("2) Change font")
        print("3) Print arts")
        print("4) Change color")
        print("5) Quit")

        choice = input("Enter choice: ")

        match(choice):
            case("1"):
                changeChr = input("Do you want use different chr? Y N :")
                if(changeChr == 'Y'or changeChr == 'y'):
                    user_char = input("Enter the characters you want to use for ASCII art: ")
                    replacement_dict = {'#': user_char[0]}
                text = input("Write text: ")
                user_art = draw_art(text,user_font,user_char)
                if(replacement_dict != None):
                    for old_char, new_char in replacement_dict.items():
                        user_art = user_art.replace(old_char, new_char)
                print(user_art)
                save = input("Save the art? Y N :")
                if(save == "Y" or save == "y"):
                    art.tsave(user_art,user_font,filename="test")

            case("2"):
                art.font_list()  
                user_font = input("Choose font: ")
                print(art.text2art(text="test",font=user_font))

            case("3"):
                print(memory)

            case("4"):
                for color in colors:
                    printArt(colored(art.text2art(text="test",font=user_font),color))

            case("5"):
                break
