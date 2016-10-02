from core import AgentCreator
import Avatar as a
import Wall as w
import Hunter as h

class GameAgentCreator(AgentCreator.AgentCreator):

    def __init__(self, gridSizeX,gridSizeY, nbWalls, nbHunters, nbAvatar=1):
        super(GameAgentCreator, self).__init__()
        self.nbWalls = nbWalls
        self.nbAvatar = nbAvatar
        self.nbHunters = nbHunters

    def create(self,x,y,env,trace,indice=-1):
        if self.nbWalls > 0 :
            self.nbWalls -= 1
            return w.Wall(x,y)
        elif self.nbHunters > 0 :
            self.nbHunters -=1
            return h.Hunter(x,y,env)
        else :
            return a.Avatar(x,y,env)