class Agent(object):
    """docstring for Agent"""
    def __init__(self):
        super(Agent, self).__init__()
    
    def decide(self) :
        raise NotImplementedError
        
    def update(self) :
        raise NotImplementedError