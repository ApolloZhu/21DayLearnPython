import math
class Elf():
    def __init__(self, name="Elf", weight = 10, height = 10, color = "blue", energy = 100):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color
        self.energy = energy
    
    def walk(self, x = 3, y = 4):
        self.energy -= math.sqrt(x*x + y*y)
        self.describe()
    
    def jump(self):
        self.energy -= 1
        self.describe()
    
    def eat(self, amount = 5):
        self.energy += amount
        self.describe()
    
    def describe(self):
        print(self.name + " with " + str(self.energy) + " energy")
