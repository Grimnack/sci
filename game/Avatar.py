from core import Agent

class Avatar(Agent.Agent):

    def __init__(self, arg):
        super(Agent, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.bougera = True
        self.futurX = None
        self.futurY = NotImplementedError

        #C'est dans la doc...
        #Peut être inutile
        self.dirX = "LUL"
        self.dirY = "xD"


    def noticeAvatar(self,dirX,dirY):
        self.dirX = dirX
        self.dirY = dirY

    def decide(self):

        (self.futurX,self.futurY) = (self.x + self.dirX, self.y + self.dirY)

        #TO DO : Option pour l'environnement torique

        if (self.env.grille[self.futurY][self.futurX] != None):
            self.bougera = True
        else
            self.bougera = False


    def update(self) :
        if self.bougera :
            self.env.grille[self.y][self.x] = None
            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY