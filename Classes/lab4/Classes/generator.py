""" Generator file"""
import logging

class ASCIIArtGenerator:
    """ Class for generatin ASCII arts"""
    def __init__(self, user_input, art_color, width, height, alignment,language):
        self.user_input = user_input
        self.art_color = art_color
        self.width = width
        self.height = height
        self.alignment = alignment
        self.ascii_art = ""
        self.language = language

    def generate_ascii_art(self):
        """ Generate arts"""
        input_lines = self.user_input.split('\n')
        max_length = max(len(line) for line in input_lines)

        self.ascii_art = [''] * len(self.language[' '])
        for i in range(len(self.language[' '])):
            for line in input_lines:
                if self.alignment == 'center':
                    line = line.center(max_length)
                elif self.alignment == 'right':
                    line = line.rjust(max_length)
                else:
                    line = line.ljust(max_length)

                for char in line:
                    char = char.upper()
                    if char in self.language:
                        self.ascii_art[i] += f'\x1b[{self.art_color}m{self.language[char][i]}\x1b[0m'
                    else:
                        self.ascii_art[i] += ' '

        self.ascii_art = '\n'.join(self.ascii_art)
        logging.info('ASSCII-art is generated')

    def display_ascii_art(self):
        """Display arts """
        print(self.ascii_art)
        logging.info('ASCII-art is displeyed')

    def save_to_file(self):
        """ Save arts"""
        save_option = input("Зберегти ASCII-арт у файлі? (Так/Н і): ").lower()
        if save_option == 'так':
            filename = input("Введіть ім'я файлу для збереження (з розширенням .txt): ")
            filepath = 'Data/' + filename
            with open(filepath,'w',encoding='utf-8') as file:
                file.write(self.ascii_art)
                print(f"ASCII-арт було збережено у файлі {filename}")
                logging.info('ASCII-art is saved')
