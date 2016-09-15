from core import SMA
import BilleCreator as bc

SMA.SMA(gridSizeX=100,gridSizeY=100,canvasSizeX=1920,canvasSizeY=1080,refresh=1,scheduling="",nbTicks=0,trace=True,grid=True,seed=None,delay=1,nbAgents=100,torique=False,agentCreator=bc.BilleCreator())
