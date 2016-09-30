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


    def noticeAvatar(self,dirX,dirY):
        self.dirX = dirX
        self.dirY = dirY

    def decide(self):
        
        (self.futurX,self.futurY) = (self.x + self.dirX, self.y + self.dirY)
        
        #TO DO : Option pour l'environnement torique

        if (self.env.grille[self.futurY][self.futurX] == None):
            self.bougera = True
        else:
            self.bougera = False

        self.update()


    def update(self) :
        if self.bougera :
            print("({},{}) -> ({},{})".format(self.x,self.y,self.futurX,self.futurY))
            self.env.grille[self.y][self.x] = None
            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY

    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='black')