from lab1.calculator import main as lab1
from lab2.main import main as lab2
from lab3.main import main as lab3
from lab4.main import main as lab4
from lab5.main import main as lab5
from lab6.main import main  as lab6
from lab7.main import main as lab7
from MenuCreator import CreateMenu

Menu = CreateMenu(title="Example Menu", elements=[
    'Lab 1: Calculator',
    'Lab 2: Main',
    'Lab 3: Main',
    'Lab 4: Main',
    'Lab 5: Main',
    'Lab 6: Main'
])

# Assuming load_menu displays the menu and wait waits for user input
Menu.load_menu()
Menu.wait()

# Assuming get_selected_item is a method that returns the index of the selected menu item
# Make sure to call it as a method with ()
selected_item = Menu.get_selected_item()

# Use the selected item to call the appropriate lab module
# Replace 'start' with the actual entry function of your lab modules
if selected_item == 'Lab 1: Calculator':
    lab1()
elif selected_item == 'Lab 2: Main':
    lab2()
elif selected_item == 'Lab 3: Main':
    lab3()
elif selected_item == 'Lab 4: Main':
    lab4()
elif selected_item == 'Lab 5: Main':
    lab5()
elif selected_item == 'Lab 6: Main':
    lab6()
