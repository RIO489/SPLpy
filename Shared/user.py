#User class
from Data.data import defaultroundto
from Data.data import memory

class User:
    def __init__(self,name):
        self.name = name
        self.roundto = defaultroundto
        self.memory = memory

    def history(self):
        for i in range (0, len(self.memory)): 
            print(self.memory[i])

    def save(self,array):
        self.memory.append(array)

    def changeRoundto(self,roundto):
        self.roundto = roundto