from modules.agents import *
from typing import *
from lb1_cleaner.mullock import *


class VacuumAgent(Agent):
    """
        A class to represent a Vacuum Cleaner.
    """
    location: List[int] = [0, 0]
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

    def moveright(self):
        self.location[0] += 1

    def moveleft(self):
        self.location[0] -= 1

    def movedown(self):
        self.location[1] += 1

    def moveup(self):
        self.location[1] -= 1

    def turn(self, d):
        self.direction = self.direction + d

    def suck(self, thing: Thing) -> bool:
        """ Returns True upon success or False otherwise. """
        return True if isinstance(thing, Dirt) else False

    def __str__(self):
        return __class__.__name__

