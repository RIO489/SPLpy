# AsciiArtGenerator.py

class AsciiArtGenerator:
    def __init__(self):
        self.figure = None

    def input_figure(self):
        # Введення користувачем параметрів 3D-фігури
        width = int(input("Enter the width of the figure: "))
        height = int(input("Enter the height of the figure: "))
        depth = int(input("Enter the depth of the figure: "))
        color1 = input("Enter the first color of the figure: ")
        color2 = input("Enter the second color of the figure: ")
        
        # Створення екземпляра класу Figure
        self.figure = Figure(width, height, depth, color1, color2)

    def manipulate_figure(self):
        # Методи для маніпулювання фігурою (масштабування, обертання тощо)
        action = input("Would you like to scale the figure? (yes/no): ")
        if action.lower() == 'yes':
            scale_factor = float(input("Enter the scale factor: "))
            self.figure.scale(scale_factor)

    def display_ascii_art(self):
        # Відображення ASCII-арту
        if self.figure is not None:
            self.figure.display_ascii_art()

    def save_to_file(self, filename):
        # Збереження ASCII-арту у текстовий файл
        if self.figure is not None and self.figure.ascii_art is not None:
            with open(filename, 'w', encoding='utf-8') as file:
                for line in self.figure.ascii_art:
                    file.write(line + '\n')
            print(f"ASCII art saved to '{filename}'.")
