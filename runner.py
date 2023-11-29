import lab1.calculator as lab1
import lab2.main as lab2
import lab3.main as lab3
import lab4.main as lab4
import lab5.main as lab5
import lab6.main as lab6
from MenuCreator import CreateMenu

Menu = CreateMenu(title="Example Menu", elements=[  
    'First element',  
    'Second element',  
    'Third element'  
])

Menu.load_menu()  
Menu.wait()

if Menu.get_selected_item == 0:
    lab1
elif Menu.get_selected_item == 1:
    lab2
elif Menu.get_selected_item == 2:
    lab3
elif Menu.get_selected_item == 3:
    lab4
elif Menu.get_selected_item == 4:
    lab5
elif Menu.get_selected_item == 5:
    lab6
