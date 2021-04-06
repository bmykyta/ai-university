from modules.agents import *


class Dirt(Thing):
    def __str__(self):
        return type(self).__name__


class Dust(Dirt):
    pass


class Jam(Dirt):
    pass


class Confetti(Dirt):
    pass
