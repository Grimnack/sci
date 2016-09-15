import random
from tkinter import *
from core import Window


class Ocean(Window.Window):

	def __init__(self, gridSizeX,gridSizeY,canvasSizeX,canvasSizeY):
		super(Ocean, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,boxSize=None,windowbg='blue',title='Simulation')
		self.sharksStats = Canvas(self.tk, width =200, height =200, bg ='white')
		self.shraksStats.pack(side=BOTTOM)

		self.fishStats = Canvas(self.tk, width =200, height =200, bg ='grey')
		self.fishStats.pack(side=RIGHT)