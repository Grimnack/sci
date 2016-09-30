from core import AgentCreator
import Avatar as a


class GameAgentCreator(AgentCreator.AgentCreator):

    def __init__(self, nbHunter=69):
        super(GameAgentCreator, self).__init__()

    def create(self,x,y,env,trace,indice=-1):
        return a.Avatar(x,y,env)