from core import Agent

class Wall(Agent.Agent):
    """docstring for Wall"""
    def __init__(self, arg):
        super(Wall, self).__init__()
        self.x = x
        self.y = y 

    def decide(self) :
        raise NotImplementedError
        
    def update(self) :
        raise NotImplementedError

    def place_agent(self,fenetre):
        raise NotImplementedError