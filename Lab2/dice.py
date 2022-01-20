"""dan Smestad video instructions lab2"""
import random

class Dice:
    def __init__(self, sides=6): #example with default set to 6. common dice set.
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

# dice = Dice(14)
# for roll in range(100): 
#     print(dice.roll())       

dice2 = Dice()
print(dice2.roll()) # exmaple with default value used here. roll() is an internal method call. 