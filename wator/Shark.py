class Shark(object):
    """docstring for Shark"""
    def __init__(self, arg):
        super(Shark, self).__init__()
                self.env = env
        self.x = x
        self.y = y
        self.trace = trace
        self.sharkBreedTime = sharkBreedTime
        self.sharkBreedTimeCPT = sharkBreedTime
        self.dontStarve = dontStarve
        self.dontStarveCPT = dontStarve
        self.bougera = True
        self.naissance = False
        self.killMe = False
        self.futurX = None
        self.futurY = None
        self.age = 0
        self.color = "pink"
      
    def randomNextPos(self) :
        lesPas = [-1,0,1]
        lesPas2LeRetour = [-1,1]
        futurX = self.x + r.choice(lesPas)
        if futurX == self.x :
            futurY = self.y + r.choice(lesPas2LeRetour)
        else :
            futurY = self.y + r.choice(lesPas)
        if self.env.torique :
            if futurY == -1 :
                futurY = len(self.env.grille)-1
            if futurY == len(self.env.grille) :
                futurY = 0
            if futurX == -1 :
                futurX = len(self.env.grille[0]) -1
            if futurX == len(self.env.grille[0]) :
                futurX = 0
        else :
            if futurY == -1 :
                futurY = 1
            if futurY == len(self.env.grille) :
                futurY = len(self.env.grille)-2
            if futurX == -1 :
                futurX = 1
            if futurX == len(self.env.grille[0]) :
                futurX = len(self.env.grille[0])-2
        return (futurX,futurY)


    """
    S'il y a des poissons dans son voisinage (torique ou pas), le requin va en manger l'un d'entre eux (et donc aller sur sa case).
    Cette fonction doit renvoyer la liste des poissons à proximité.
    [(x,y),(z,t),etc] en cas de poissons, [] sinon
    """
    def whereIsTheFish(self):
    	return []

    def decide(self) :
        """
        on choisis un pas random et on observe si il y a un obstacle ou pas
        """

        #RIP in spaghettis, never forgetti
        if self.sharkBreedTimeCPT == 0:
        	self.killMe = True
        	self.update()
        	return


        (self.futurX,self.futurY) = self.randomNextPos()
        if (len(self.whereIsTheFish()) > 0):
        	print("Miam Miam KFF")
        	self.dontStarveCPT = self.dontStarve
        else
        	self.dontStarveCPT = self.dontStarveCPT - 1
        
        if (isinstance(self.env.grille[futurY][futurX],Shark)) :
            self.bougera = False
        else :
            self.bougera = True

        if self.sharkBreedTimeCPT == 0 :
            self.naissance = True
            self.sharkBreedTimeCPT = self.sharkBreedTime
        else :
            self.sharkBreedTimeCPT -= 1



    def update(self) :
        """
        ATTENTION
        Problematique actuelle comment faire en sorte d'ajouter notre nouveau poisson à la liste des agents ?
        Contenir la liste des Agents dans l'environnement ;) IZI GAME IZI LIFE
        """

        if self.killMe:
        	self.env.grille[self.y][self.x] = None
        #Faut absolument prévenir SMA pour supprimer le requin de la liste lesAgents.
        #Etre bourrin et donner SMA en attribut d'un agent ? Bof, vraiment bof et ça peut faire un Concurrent Modification Error peut-être.

        self.age += 1
        self.color = "red"

        if self.bougera :
            if self.naissance :
                self.env.grille[self.y][self.x] = Shark(self.x,self.y,self.env,self.trace,self.sharkBreedTime)
                self.naissance = False
            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY

        # TODO TODO TODO TODO TODO 