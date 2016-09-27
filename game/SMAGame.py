from core import Environnement as env
from core import Agent
from core import Window as w
from core import SMA
import random
import time
from tkinter import *


class SMAGame(SMA.SMA):

    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre):
        super(SMAWator, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre)

        self.fenetre.can.focus_set()
        self.fenetre.can.bind("<Left>",self.avatarLeft)
        self.fenetre.can.bind("<Right>",self.avatarRight)
        self.fenetre.can.bind("<Up>",self.avatarUp)
        self.fenetre.can.bind("<Down>",self.avatarDown)

    def run(self):
        super(SMAGame, self).run()

    def avatarLeft(self,event):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar)): #if (isinstance(agent,Avatar.Avatar)): ?
                agent.notice(-1,0)