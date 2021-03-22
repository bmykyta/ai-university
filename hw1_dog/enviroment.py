from hw1_dog.things import *
from typing import List


class Park(Environment):
    def percept(self, agent: Agent) -> List[Thing]:
        """ Returns a list of things that are in our agent's location. """
        things = self.list_things_at(agent.location)
        return things

    def execute_action(self, agent: Agent, action: str):
        """ Changes the state of the environment based on what the agent does. """
        if action == 'move down':
            print(f"{agent} decided to {action} at location {agent.location}")
            agent.movedown()
        elif action == 'eat':
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]):
                    print(f"{agent} ate at location: {agent.location}")
                    self.delete_thing(items[0])
        elif action == 'drink':
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]):
                    print(f"{agent} drank at location: {agent.location}")
                    self.delete_thing(items[0])

    def is_done(self):
        """ By default, we're done when we can't find a live agent, but to prevent killing out cute dog, we will stop
        before itself - when there is no more food or water """
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)

        return dead_agents or no_edibles
