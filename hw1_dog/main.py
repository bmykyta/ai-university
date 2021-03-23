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
        if isinstance(p, Bump):
            turn = False
            choice = random.choice((1, 2))
        else:
            choice = random.choice((1, 2, 3, 4))
            # choice = int(input("Enter 1-4: ")) # manual control of certain object

    if choice == 1:
        return 'turnright'
    elif choice == 2:
        return 'turnleft'
    else:
        return 'moveforward'


park = Park2D(5, 5, color={'BlindDog': (200, 0, 0), 'Water': (0, 200, 200), 'Food': (230, 115, 40)})
dog = BlindDog(program)
dogFood = Food()
water = Water()
park.add_thing(dog, [0, 0])
park.add_thing(dogFood, [1, 3])
park.add_thing(water, [0, 1])
morewater = Water()
morefood = Food()
park.add_thing(morewater, [3, 4])
park.add_thing(morefood, [4, 0])
print("BlindDog starts at [0,0] facing downwards, lets see if he can find any food!")
park.run(20)
