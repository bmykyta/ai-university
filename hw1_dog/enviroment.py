from hw1_dog.things import *
from typing import List


class Park2D(GraphicEnvironment):
    def percept(self, agent: Agent) -> List[Thing]:
        """ Returns a list of things that are in our agent's location. """
        things = self.list_things_at(agent.location)
        loc = copy.deepcopy(agent.location)

        if agent.direction.direction == Direction.R:
            loc[0] += 1
        elif agent.direction.direction == Direction.L:
            loc[0] -= 1
        elif agent.direction.direction == Direction.D:
            loc[1] += 1
        elif agent.direction.direction == Direction.U:
            loc[1] -= 1
        if not self.is_inbounds(loc):
            things.append(Bump())

        return things

    def execute_action(self, agent: Agent, action: str):
        """ Changes the state of the environment based on what the agent does. """
        if action == 'moveforward':
            print(f"{agent} decided to {action} at location {agent.location}")
            agent.moveforward()
        elif action == 'turnright':
            print(f"{agent} decided to {agent.direction.direction} at location {agent.location}")
            agent.turn(Direction.R)
            # agent.moveforward() # if you wanna mannualy control dog object
        elif action == 'turnleft':
            print(f"{agent} decided to {agent.direction.direction} at location {agent.location}")
            agent.turn(Direction.L)
            # agent.moveforward() # if you wanna mannualy control dog object
        elif action == 'eat':
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]):
                    print(f"{agent} ate {items[0]} at location: {agent.location}")
                    self.delete_thing(items[0])
        elif action == 'drink':
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]):
                    print(f"{agent} drank {items[0]} at location: {agent.location}")
                    self.delete_thing(items[0])

    def is_done(self):
        """ By default, we're done when we can't find a live agent, but to prevent killing out cute dog, we will stop
        before itself - when there is no more food or water """
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)

        return dead_agents or no_edibles