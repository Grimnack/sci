import sys
sys.path.append('..')

import SMAGame as sma
from core import Window as w
import GameAgentCreator as ga


gridSizeX=50
gridSizeY=50
canvasSizeX=800
canvasSizeY=600

nbWalls = 50
nbHunters = 3


initGame = ga.GameAgentCreator(gridSizeX,gridSizeY,nbWalls,nbHunters)
fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY,boxSize=None,windowbg='ivory',title="Simulation de particules")

sma.SMAGame(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling="fair"
    ,nbTicks=0
    ,trace=False
    ,grid=False
    ,seed=None
    ,delay=200
    ,nbAgents=nbHunters + nbWalls+ 1#initGame.nbAgents()
    ,fenetre=fenetre
    ,torique=True
    ,agentCreator=initGame
    ).run()