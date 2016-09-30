from core import AgentCreator
import Avatar as a


class GameAgentCreator(AgentCreator.AgentCreator):

    def __init__(self, gridSizeX,gridSizeY, nbHunters=69):
        super(GameAgentCreator, self).__init__()
        self.nbWalls = 2 * gridSizeX + 2 * gridSizeY - 4
        self.nbAvatar = 1
        self.nbHunters = nbHunters

    def create(self,x,y,env,trace,indice=-1):
        return a.Avatar(x,y,env)

    def nbAgents(self):
        return self.nbWalls + self.nbAvatar + self.nbHunters