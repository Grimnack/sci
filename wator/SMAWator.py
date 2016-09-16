from core import Environnement as env
from core import Agent
from core import Window as w
from core import SMA
import random
import time
from tkinter import *



class SMAWator(SMA.SMA):

    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre):
        super(SMAWator, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre)

    def run(self):
        super(SMAWator, self).run()

    def printf(self):
        super(SMAWator, self).printf()

        fishes = sharks = 0
        for agent in self.env.lesAgents:
            if agent.isFish():
                fishes += 1
            else:
                sharks += 1


        self.fenetre.showTicks.delete('text')   
        self.fenetre.fishStats.delete('text')   
        self.fenetre.sharkStats.delete('text')      

        self.fenetre.showTicks.create_text(100,100,text='Tour n°'+str(self.nbActualTicks),tag='text') 
        self.fenetre.fishStats.create_text(100,100,text='Poissons\n'+str(fishes),tag='text')    
        self.fenetre.sharkStats.create_text(100,100,text='Requins\n'+str(sharks),tag='text')

    def theloop(self):
        super(SMAWator, self).theloop()
