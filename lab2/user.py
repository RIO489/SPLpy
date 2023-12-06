from lab2.data import defaultroundto
from lab2.data import memory

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