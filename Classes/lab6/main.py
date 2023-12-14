""" Main file"""
import unittest
from .classes.test import TestCalculator

def main():
    """ Main method"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

    runner = unittest.TextTestRunner()

    runner.run(suite)

if __name__ == "__main__":
    main()
