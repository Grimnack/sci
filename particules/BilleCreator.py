from particules import Bille as b
from core import AgentCreator

class BilleCreator(AgentCreator.AgentCreator):
    """docstring for BilleCreator"""
    def __init__(self):
        super(BilleCreator, self).__init__()

    def create(self,indice,x,y,env,trace) :
        return b.Bille(indice,x,y,env,trace)
        