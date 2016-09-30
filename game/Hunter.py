from core import Agent
import Avatar 
import random

class Hunter(Agent.Agent):
    """docstring for Hunter"""
    def __init__(self, x,y,env):
        super(Hunter, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.bougera = True
        self.futurX = None
        self.futurY = None  
        

    def thePositionsToWatch(self) :
        nord = (self.x,self.y-1)
        sud = (self.x,self.y+1)
        est = (self.x+1,self.y)
        ouest = (self.x-1,self.y)
        lesPos = [nord,sud,est,ouest]
        res = []
        for (x,y) in lesPos :
            finalX = x
            finalY = y
            if x == -1 :
                finalX = len(self.env.grille[0])-1
            elif x == len(self.env.grille[0]) :
                finalX = 0
            if y == -1 :
                finalY = len(self.env.grille) -1 
            elif y == len(self.env.grille) :
                finalY = 0
            # Soit c est un environnement torique 
            # Soit on ne souhaite pas sortir du cadre 
            # donc on a pas fait de modifications
            if self.env.torique or (finalX == x and finalY == y) :
                res.append((finalX,finalY))
        return res 
            
    def decide(self) :
        """
        Se déplace dans le voisinage de von neuman 
        Se dirige vers la case numéroté le plus faiblement.
        """
        lesPos = self.thePositionsToWatch()
        random.shuffle(lesPos)
        minX = None
        minY = None
        minScore = None
        for (x,y) in lesPos :    
            score = self.env.score[y][x]
            if minScore == None :
                if score < self.env.score[self.y][self.x] :
                    minScore = score
                    minX = x
                    minY = y
            elif minScore > score :
                minScore = score
                minX = x
                minY = y
        if minScore == None :
            self.bougera = False
        else :
            self.bougera = True
            self.futurX = minX
            self.futurY = minY

        self.update()



    def update(self) :
        if self.bougera :
            #print("Hunter : ({},{}) -> ({},{})".format(self.x,self.y,self.futurX,self.futurY))
            self.env.grille[self.y][self.x] = None

            if ((self.env.grille[self.futurY][self.futurX] != None) and isinstance(self.env.grille[self.futurY][self.futurX],Avatar.Avatar)):
                self.env.kill(self.env.grille[self.futurY][self.futurX])

            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY
    
    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
      

    def place_agent(self,fenetre):
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='red')