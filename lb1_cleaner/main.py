from lb1_cleaner.vacuum_environment import *
from lb1_cleaner.vacuum_agent import *

color = {
    'Glitter': (195, 7, 247), # purple
    'Wall': (82, 250, 239),
    'Dirt': (100, 101, 102), # grey
    'Jam': (242, 0, 77), # crimson
    'Confetti': (250, 152, 5), # orange
    'VacuumAgent': (33, 122, 255),
}

turn = False


def program(percepts):
    """ Return an action based on the dog's percepts """
    global turn
    print(percepts)
    for p in percepts:
        if isinstance(p, Dirt):
            return 'Suck'
        elif isinstance(p, Wall):
            turn = not turn
            return 'Left' if turn else 'Right'
        # elif isinstance(p, Bump):
        #     turn = not turn
        #     return 'Left' if turn else 'Right'
        else:
            return 'Rectilinear'
            # return 'Spiral'


width = 10
height = 10
vacuum_env = VacuumCleanerEnvironment(color=color)
vacuum = VacuumAgent(program)
vacuum_env.add_thing(vacuum, [1, 1])
n = random.randrange(5, 25)
for i in range(n):
    dirt = random.choice((Glitter, Jam, Confetti))
    loc_x = random.randrange(2, width - 1)
    loc_y = random.randrange(1, height - 1)
    loc = [loc_x, loc_y]
    if not vacuum_env.list_things_at(loc, tclass=Dirt):
        vacuum_env.add_thing(dirt(), loc)

vacuum_env.run(width*height, 1)
# vacuum_env.run(1, 1)
print(f"Agent performance: {vacuum.performance}")
