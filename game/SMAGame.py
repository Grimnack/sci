from core import Environnement as env
from core import Agent
from core import Window as w
from core import SMA
import Wall as wall
import random
import time
from tkinter import *


class SMAGame(SMA.SMA):

    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre):
        super(SMAWator, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre)
        
        #Ajout des murs (au bord de la fenetre pour l'instant)
        for y in range(len(gridSizeY)) :
            for x in range(len(gridSizeX)) :
                if((y == 0) or (y == (gridSizeY - 1)) or (x == 0) or (x == (gridSizeX - 1)) ) :
                    newWall = wall.Wall(x,y)
                    self.env.ajouteAgent(newWall)

        self.fenetre.can.focus_set()
        self.fenetre.can.bind("<Left>",self.avatarLeft())
        self.fenetre.can.bind("<Right>",self.avatarRight())
        self.fenetre.can.bind("<Up>",self.avatarUp())
        self.fenetre.can.bind("<Down>",self.avatarDown())

    def run(self):
        super(SMAGame, self).run()

    def avatarLeft(self):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar)): #if (isinstance(agent,Avatar.Avatar)): ?
                agent.noticeAvatar(-1,0)

    def avatarRight(self):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar)): #if (isinstance(agent,Avatar.Avatar)): ?
                agent.noticeAvatar(1,0)

    def avatarUp(self):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar)): #if (isinstance(agent,Avatar.Avatar)): ?
                agent.noticeAvatar(0,-1)

    def avatarDown(self):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar)): #if (isinstance(agent,Avatar.Avatar)): ?
                agent.noticeAvatar(0,1)