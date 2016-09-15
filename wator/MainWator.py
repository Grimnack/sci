from core import SMA
import Ocean as o

gridSizeX=100
gridSizeY=100
canvasSizeX=800
canvasSizeY=600


ocean = o.Ocean(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)
ocean.tk.mainloop()