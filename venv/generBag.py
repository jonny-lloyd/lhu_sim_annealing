import random
from items import *

def generateBag():
    bag = []
    for item in items:
        randChoice = random.randint(0, 1)
        if randChoice == 1:  # selecting whether items are chosen or not, randomly
            bag.append(item)
    return bag
