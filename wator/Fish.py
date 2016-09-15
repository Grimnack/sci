class Fish(object):
    """docstring for Fish"""
    def __init__(self,indice,x,y,env,trace,fishBreedTime):
        super(Fish, self).__init__()
        self.env = env
        self.x = x
        self.y = y
        self.trace = trace
        self.indice = indice
        self.fishBreedTime = fishBreedTime


    def decide(self) :
        pass


    def update(self) :
        pass 
        