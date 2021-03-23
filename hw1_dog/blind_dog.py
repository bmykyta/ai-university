from hw1_dog.things import *
from modules.agents import *
from typing import List


class BlindDog(Agent):
    """
    A class to represent a Blind Dog.
    """
    location: List[int] = [0, 1]
    direction = Direction("down")

    def moveforward(self, success=True):
        """ Move forward possible only if success (i.e. valid destination location). """
        if not success:
            return
        if self.direction.direction == Direction.R:
            self.location[0] += 1
        elif self.direction.direction == Direction.L:
            self.location[0] -= 1
        elif self.direction.direction == Direction.D:
            self.location[1] += 1
        elif self.direction.direction == Direction.U:
            self.location[1] -= 1

    def turn(self, d):
        self.direction = self.direction + d

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
