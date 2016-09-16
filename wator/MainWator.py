import SMAWator as sma
import Ocean as o
import FishAndSharkCreator as wildLife

gridSizeX=50
gridSizeY=50
canvasSizeX=800
canvasSizeY=600
nbFish=200
nbShark=5

ocean = o.Ocean(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)
#ocean.tk.mainloop()

sma.SMAWator(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling="fair"
    ,nbTicks=0
    ,trace=False
    ,grid=True
    ,seed=None
    ,delay=100
    ,nbAgents=nbFish+nbShark
    ,fenetre=ocean
    ,torique=False
    ,agentCreator=wildLife.FishAndSharkCreator(nbFish,nbShark,2,10,3)
    )


#SMA(FishandSharkCreator(a,b),nbAgents=a+b)