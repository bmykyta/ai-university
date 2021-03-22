from hw1_dog.things import *
from modules.agents import *


class BlindDog(Agent):
    """
    A class to represent a Blind Dog.
    """
    location: int = 1

    def movedown(self):
        self.location += 1

    def eat(self, thing: Thing) -> bool:
        """ Returns True upon success or False otherwise. """
        if isinstance(thing, Food):
            return True
        return False

    def drink(self, thing: Thing) -> bool:
        """ Returns True upon success or False otherwise. """
        if isinstance(thing, Water):
            return True
        return False

    def __str__(self):
        return __class__.__name__
