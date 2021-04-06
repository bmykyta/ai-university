from lb1_cleaner.vacuum_agent import *
from typing import *


class VacuumCleanerEnvironment(GraphicEnvironment):
    perceptible_distance: int = 1
    isForward: bool = True
    isLeft: bool = False
    isRight: bool = True
    isUp: bool = False
    isDown: bool = False

    def __init__(self, width=10, height=10, boundary=True, color={}, display=False):
        super().__init__(width, height, boundary, color, display)
        self.add_walls()

    def thing_classes(self):
        """ List of classes that can go into environment. """
        return [Wall, Dirt, Jam, Confetti, ReflexVacuumAgent, ModelBasedVacuumAgent, VacuumAgent]

    def things_near(self, location, radius=None):
        """Return all things within radius of location."""
        if radius is None:
            radius = self.perceptible_distance
        radius2 = radius * radius
        return [(thing, radius2 - distance_squared(location, thing.location))
                for thing in self.things if distance_squared(
                location, thing.location) <= radius2]

    def percept(self, agent: VacuumAgent) -> List[Thing]:
        """ Returns a list of things that are in our agent's location. """
        things = self.list_things_at(agent.location)
        loc = copy.deepcopy(agent.location)

        if not self.is_inbounds(loc):
            things.append(Bump())

        return things

    def __suck_if_dirty(self, agent: VacuumAgent):
        items = self.list_things_at(agent.location, tclass=Dirt)
        isDirt = False
        if items:
            dirt = items[0]
            if agent.suck(dirt):
                isDirt = True
                agent.performance += 100
                self.delete_thing(dirt)
        return isDirt

    def rectilinear_locomotion(self, agent: VacuumAgent):
        loc = copy.deepcopy(agent.location)
        col = self.height - 1
        isMovedDown: bool = False
        if not self.__suck_if_dirty(agent):
            if self.isForward:
                agent.moveright()
            else:
                agent.moveleft()

    def spiral_locomotion(self, agent: VacuumAgent):
        loc = copy.deepcopy(agent.location)
        row = self.width - 3
        column = self.height - 3
        isFirst = True
        canEat = False

        for i in range(row):

            if isFirst:
                j = i
                isFirst = not isFirst
            else:
                j = i - 1

            while j < column - i:
                if not self.__suck_if_dirty(agent):
                    agent.moveright()
                    j += 1
                self.update(1)

            k = i
            while k < row - i:
                if not self.__suck_if_dirty(agent):
                    agent.movedown()
                    k += 1
                self.update(1)

            j = column - i - 1
            while j >= i:
                if not self.__suck_if_dirty(agent):
                    agent.moveleft()
                    j -= 1
                self.update(1)

            k = row - i - 1
            while k > i:
                if not self.__suck_if_dirty(agent):
                    agent.moveup()
                    k -= 1
                self.update(1)

    def execute_action(self, agent: VacuumAgent, action: str):
        """ Changes the state of the environment based on what the agent does. """
        if action == 'Rectilinear':
            agent.performance -= 1
            self.rectilinear_locomotion(agent)
        elif action == 'Spiral':
            agent.performance -= 1
            self.spiral_locomotion(agent)
        elif action == 'Suck':
            items = self.list_things_at(agent.location, tclass=Dirt)
            if items:
                dirt = items[0]
                agent.suck(dirt)
                agent.performance += 10
                print(f"{agent} clean {dirt} at location: {agent.location}")
                self.delete_thing(dirt)
        elif action == 'Left':
            self.isForward = False
            agent.movedown()
            self.rectilinear_locomotion(agent)
        elif action == 'Right':
            self.isForward = True
            agent.movedown()
            self.rectilinear_locomotion(agent)

    def is_done(self):
        no_edibles = not any(isinstance(thing, Dirt) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)

        return dead_agents or no_edibles