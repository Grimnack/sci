from core import Agent

class Avatar(Agent.Agent):

    def __init__(self, x,y,env):
        super(Avatar, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.bougera = True
        self.futurX = None
        self.futurY = None

        #C'est dans la doc...
        #Peut être inutile
        self.dirX = 0
        self.dirY = 0
        self.quatreDir = [(0,1),(0,-1),(-1,0),(1,0)]

        self.calculeScore()

    def isWall(self) :
        return False
    def isAvatar(self) :
        return True

    def getVoisins(self,x,y) :
        lesVoisins = []
        for (pasX,pasY) in self.quatreDir :
            (futurX,futurY) = (pasX + x, pasY + y)
            if not ((futurX == -1) or (futurY == -1) or (futurX == len(self.env.grille[0])) or (futurY == len(self.env.grille))) :
                if self.env.score[futurY][futurX] == None :
                    lesVoisins.append((futurX,futurY))
        return lesVoisins

    def calculeScore(self) :
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
                    if self.env.grille[futurY][futurX] == None or not self.env.grille[futurY][futurX].isWall:
                        self.env.score[futurY][futurX] = self.env.score[y][x] + 1
                        tmp.append((futurX,futurY))
            positions = tmp[:]

    def noticeAvatar(self,dirX,dirY):
        self.dirX = dirX
        self.dirY = dirY

    def decide(self):
        # print("Avatar decide")
        print(self.env.score)
        (self.futurX,self.futurY) = (self.x + self.dirX, self.y + self.dirY)
        
        #TO DO : Option pour l'environnement torique

        if (self.env.grille[self.futurY][self.futurX] == None):
            self.bougera = True
        else:
            self.bougera = False

        self.update()


    def update(self) :
        if self.bougera :
            #print("({},{}) -> ({},{})".format(self.x,self.y,self.futurX,self.futurY))
            self.env.grille[self.y][self.x] = None
            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY
            self.calculeScore()


    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='black')