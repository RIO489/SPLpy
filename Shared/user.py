"""User class"""
import logging
from Data.data import DEFAULT_ROUNDTO
from Data.data import memory

class User:
    """ User class"""
    def __init__(self,name):
        self.name = name
        self.roundto = DEFAULT_ROUNDTO
        self.memory = memory

    def history(self):
        """ print memory"""
        for value in self.memory:
            print(value)

    def save(self,array):
        """ save memory"""
        self.memory.append(array)
        logging.info("Calculation is saved %s",array)

    def change_roundto(self,roundto):
        """ Change round to"""
        self.roundto = roundto
