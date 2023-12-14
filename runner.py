""" Main runner"""
import logging
from Classes.lab1.main import main as lab1
from Classes.lab2.main import main as lab2
from Classes.lab3.main import main as lab3
from Classes.lab4.main import main as lab4
from Classes.lab5.main import main as lab5
from Classes.lab6.main import main as lab6
from Classes.lab7.classes.bot import main as lab7
from Classes.lab8.main import main as lab8
from MenuBuilder.Menu import Menu

menu_items = [
    ("Lab 1: Calculator", lab1),
    ("Lab 2: OOP Calculator", lab2),
    ("Lab 3: ASCII-art", lab3),
    ("Lab 4: ASCII-art without libraries",lab4),
    ("Lab 5: ASCII-art with 3D figures",lab5),
    ("Lab 6: Calculator unittest",lab6),
    ("Lab 7: Telegrab Bot API",lab7),
    ("Lab 8: Dota 2 mathes analysis",lab8)
]
class LabFacade:
    """Class that suing Facade pattern"""
    def __init__(self, items):
        self.menu = Menu("Main Menu", items)

    def run_lab(self, lab_number):
        """Run labs main file method """
        # Map the lab numbers to the corresponding functions
        lab_functions = {
            1: lab1,
            2: lab2,
            3: lab3,
            4: lab4,
            5: lab5,
            6: lab6,
            7: lab7,
            8: lab8
        }
     # Run the selected lab function
        lab_function = lab_functions.get(lab_number)
        if lab_function:
            lab_function()
        else:
            print(f"Lab {lab_number} is not available.")

    def run(self):
        """Method to launch the code"""
        logging.basicConfig(filename='Data/logger.log', filemode='w', level=logging.DEBUG)
        while True:
            self.menu.display()
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    print("Exiting...")
                    break
                else:
                    self.run_lab(choice)
            else:
                print("Invalid choice. Please enter a number.")
            input("Press Enter to continue...")

# The main function now just creates the facade and calls its run method
def main():
    """Main method """
    facade = LabFacade(menu_items)
    facade.run()

if __name__ == '__main__':
    main()
