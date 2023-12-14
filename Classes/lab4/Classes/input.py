"""This module is responsible for handling correct inputs"""
import logging
from Shared.exception import IncorrectArgumentException
from Data.languages import english_font, ukraine_font

class InputHandler:
    """Handles user input for generating ASCII art."""

    def get_user_input(self, input_value):
        """
        Validates if the input value contains only alphabetic characters.

        Args:
            input_value (str): The user-provided input value.

        Returns:
            str: The validated input value.

        Raises:
            IncorrectArgumentException: If the input contains non-alphabetic characters.
        """
        if input_value.isalpha():
            return input_value
        else:
            logging.warning('Input value is not correct %s', input_value)
            raise IncorrectArgumentException("Input must contain only alphabetic characters.")

    def get_art_size(self, input_width, input_height):
        """
        Validates and converts the width and height inputs into integers.

        Args:
            input_width (str): The user-provided width value.
            input_height (str): The user-provided height value.

        Returns:
            list: The validated width and height as integers.

        Raises:
            IncorrectArgumentException: If the inputs are not digits.
        """
        if input_width.isdigit() and input_height.isdigit():
            width = int(input_width)
            height = int(input_height)
        else:
            logging.warning('Input values are not correct: %s, %s', input_width, input_height)
            raise IncorrectArgumentException("Inputs must contain only digits.")

        return [width, height]

    def get_alignment(self, input_value):
        """
        Validates if the input value is a valid text alignment option.

        Args:
            input_value (str): The user-provided alignment value.

        Returns:
            str: The validated alignment option.

        Raises:
            IncorrectArgumentException: If the input is not 'left', 'center', or 'right'.
        """
        if input_value.isalpha() and input_value in ['left', 'center', 'right']:
            return input_value
        else:
            logging.warning('Input value is not correct %s', input_value)
            raise IncorrectArgumentException("Must be characters and in range [left,center,right].")

    def get_color(self, input_value):
        """
        Validates if the input value is a valid ASCII art color.

        Args:
            input_value (str): The user-provided color value.

        Returns:
            str: The validated color.

        Raises:
            IncorrectArgumentException: If the input is not '@', '#', or '*'.
        """
        if input_value in ['@', '#', '*']:
            return input_value
        else:
            logging.warning('Input value is not correct %s', input_value)
            raise IncorrectArgumentException("Input must be in range [@,#,*] characters.")

    def get_language(self, input_value):
        """
        Validates the input value for language selection and returns the corresponding font.

        Args:
            input_value (str): The user-provided language value.

        Returns:
            list: The font corresponding to the chosen language.

        Raises:
            IncorrectArgumentException: If the input is not 'eng' or 'ukr'.
        """
        if input_value in ['eng', 'ukr']:
            return english_font if input_value == 'eng' else ukraine_font
        else:
            logging.warning('Input value is not correct %s', input_value)
            raise IncorrectArgumentException("Input must be 'eng' or 'ukr'.")

    def get_answer(self, user_control):
        """
        Validates if the input value is a valid response for continuation control.

        Args:
            user_control (str): The user-provided control response.

        Returns:
            str: The validated response.

        Raises:
            IncorrectArgumentException: If the input is not 'Y', 'y', 'yes', 'N', 'n', or 'no'.
        """
        if user_control in ['Y', 'y', 'yes', 'N', 'n', 'no']:
            return user_control
        else:
            logging.warning('Input value is not correct %s', user_control)
            raise IncorrectArgumentException("Must be in range ['Y', 'y', 'yes', 'N', 'n', 'no'].")
