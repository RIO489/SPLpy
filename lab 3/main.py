import art
import pyfiglet

#data.py
user_font = "standart"
user_art = ""
memory = []


def save_art(art):
    memory.append(art)

#Main calculations
while(1):
    print("1) Enter text")
    print("2) Change font")
    print("3) Print arts")
    print("4) Quit")

    choice = input("Enter choice: ")
    
    match(choice):
        case("1"):
            text = input("Write text: ")
            user_art = art.text2art(text,user_font)
            print(user_art)
            save = input("Save the art? Y N :")
            if(save == "Y" or save == "y"):
                art.tsave(user_art,user_font)

        case("2"):
            art.font_list()  
            user_font = input("Choose font: ")
            print(art.text2art(text="test",font=user_font))

        case("3"):
            print(memory)

        case("4"):
            break
