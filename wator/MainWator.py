from core import SMA
import Ocean as o
import FishAndSharkCreator as wildLife

gridSizeX=100
gridSizeY=100
canvasSizeX=800
canvasSizeY=600


ocean = o.Ocean(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)
ocean.tk.mainloop()

SMA.SMA(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling=""
    ,nbTicks=0
    ,trace=True
    ,grid=True
    ,seed=None
    ,delay=1
    ,nbAgents=100
    ,fenetre=fenetre
    ,torique=False
    ,agentCreator=wildLife.FishAndSharkCreator()
    ,title="Préfecture du golfe"
    )


#SMA(FishandSharkCreator(a,b),nbAgents=a+b)