from random import randint

class Food:
    def __init__(self):
        self.location = [randint(0,59)*10, randint(0,39)*10]
        
    def respawn_parameter(self):
        self.location = [randint(0,59)*10, randint(0,39)*10]
        