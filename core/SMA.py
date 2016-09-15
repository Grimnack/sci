from core import Environnement as env
from core import Agent
from core import Window as w
import random
import time
from tkinter import *



class SMA(object):
    """docstring for SMA
    Il n'y a pas d'implementation en python mais on lui donne le même comportement qu'un observable
    """
    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre,title='Simulation'):

        if ( (gridSizeX * gridSizeY) < nbAgents ):
            print("Pas assez d'espace pour placer les "+str(nbAgents)+" agents.\nEssayez un plus petit nombre ("+str(gridSizeX * gridSizeY)+" ou moins).")
            return

        super(SMA, self).__init__()
        self.env = env.Environnement(gridSizeX,gridSizeY,torique=torique)
        self.delay = delay
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.nbActualTicks = 0
        self.trace = trace
        self.refresh = refresh
        self.grid = grid
        self.lesAgents = []
        
        #self.colors = ['red','firebrick', 'magenta2','green','yellow','magenta','blue','black', 'chocolate']
        #indiceColor = 0
        random.seed(seed)
        self.fenetre = fenetre
        if self.grid:
            self.fenetre.grille()
        for i in range(nbAgents) :
            (x,y) = self.env.getFreeXYAlea()
            agent = agentCreator.create(i,x,y,self.env,self.trace)
            agent.place_agent(self.fenetre)
            self.env.ajouteAgent(agent)
            self.lesAgents.append(agent)

        if self.trace:
            print("Placement aléatoire des billes (tour 0)")

        self.run()

    def run(self):
        self.fenetre.can.after(self.delay,self.theloop)
        self.fenetre.can.mainloop()

    def theloop(self):

        self.nbActualTicks = self.nbActualTicks + 1

        # 1. Les billes décident de leur nouvelles positions. L'ordre de décision est séquentiel (toujours la même balle en premier) ou aléatoire.
        if self.scheduling in ("chaos","unfair","rand","aleatoire","alea","aléatoire"):
            for i in range(len(self.lesAgents)):
                agent = random.choice(self.lesAgents)
                agent.decide()
        elif self.scheduling in ("fair"):
            random.shuffle(self.lesAgents)
            for agent in self.lesAgents:
                agent.decide()

        # 2. Mise à jour de l'affichage tous les refresh ticks. Si refresh = 1, l'affichage est mis à jour à chaque fin de tick.
        if(self.nbActualTicks % self.refresh) == 0 :     
            self.fenetre.can.delete("agent")
            self.fenetre.can.delete("text")
            for agent in self.lesAgents :
                agent.place_agent(self.fenetre)

        if self.trace:
            print("Fin du tour n°"+str(self.nbActualTicks))

        # 3. Terminaison
        # 0 = infini
        # Sinon voir si on a atteint le nombre de ticks demandés par l'utilisateur
        
        if((self.nbTicks==0) or (self.nbActualTicks < self.nbTicks)):
            self.fenetre.can.after(self.delay,self.theloop)
        else :
            self.fenetre.tk.destroy()








