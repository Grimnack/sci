from core import SMA
from core import Window as w
import BilleCreator as bc

gridSizeX=100
gridSizeY=100
canvasSizeX=800
canvasSizeY=600


fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY,boxSize=None,windowbg='ivory',title="Simulation de particules")

SMA.SMA(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling="chaos"
    ,nbTicks=0
    ,trace=True
    ,grid=True
    ,seed=None
    ,delay=1
    ,nbAgents=100
    ,fenetre=fenetre
    ,torique=False
    ,agentCreator=bc.BilleCreator()
    ).run()
