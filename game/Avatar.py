from core import Agent

class Avatar(Agent.Agent):

    def __init__(self, arg):
        super(Agent, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.bougera = True
        self.futurX = None
        self.futurY = None

        #C'est dans la doc...
        #Peut être inutile
        self.dirX = "LUL"
        self.dirY = "xD"
        self.quatreDir = [(0,1),(0,-1),(-1,0),(1,0)]

    def getVoisins(self,x,y) :
        lesVoisins = []
        for (pasX,pasY) in self.quatreDir :
            (futurX,futurY) = (pasX + x, pasY + y)
            if not (futurX == -1 or futurY == -1 or futurX == len(self.env.grille[0]) or futurY == len(self.env.grille)) :
                if self.env.score[y][x] == None :
                    lesVoisins.append((futurX,futurY))
        return lesVoisins

    def calculScore(self) :
        '''
        
        '''
        self.env.score = []
        for i in range(len(self.env.grille)) :
            self.env.score.append([None] * len(self.env.grille[0]))
        self.env.score[self.y][self.x] = 0
        positions = [(self.x,self.y)]
        while not positions == []:
            tmp = []
            for (x,y) in positions :
                lesVoisins = self.getVoisins(x,y)
                for (futurX,futurY) in lesVoisins :
                    self.env.score[futurY][futurX] = self.env.score[y][x] + 1
                    tmp.append((futurX,futurY))
            positions = tmp[:]



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