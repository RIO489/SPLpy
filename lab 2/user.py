from data import defaultroundto
from data import memory

#User class
class User:
    def __init__(self,name):
        self.name = name
        self.roundto = defaultroundto
        self.memory = memory

    def save(self,array):
        self.memory.append(array)

    def changeRoundto(self,roundto):
        self.roundto = roundto