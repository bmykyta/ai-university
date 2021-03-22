from hw1_dog.blind_dog import *
from hw1_dog.enviroment import *
from hw1_dog.things import *
from typing import *


def program(percepts):
    """ Return an action based on the dog's percepts """
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'move down'


park = Park()
dog = BlindDog(program)
dogFood = Food()
water = Water()
park.add_thing(dog, 1)
park.add_thing(dogFood, 5)
park.add_thing(water, 7)

park.run(10)
