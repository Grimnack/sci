from core import AgentCreator
import Fish as f
import Shark as s
import random

class FishAndSharkCreator(AgentCreator.AgentCreator):
    """docstring for FishAndSharkCreator"""
    def __init__(self, nbFish, nbShark, fishBreedTime, sharkBreedTime,sharkStarveTime):
        super(FishAndSharkCreator, self).__init__()
        self.nbFish = nbFish
        self.nbShark = nbShark
        self.fishBreedTime = fishBreedTime
        self.sharkBreedTime = sharkBreedTime
        self.sharkStarveTime = sharkStarveTime
        

    def create(self,indice,x,y,env,trace) :
        if (self.nbFish == 0) and (self.nbShark == 0) :
            raise "ERROR FishAndSharkCreator : Limite d agents dépassée"
        elif self.nbFish == 0 :
            return s.Shark(indice,x,y,env,trace,self.sharkBreedTime,self.sharkStarveTime)
        elif self.nbShark == 0 :
            return f.Fish(indice,x,y,env,trace,self.fishBreedTime)
        else :
            shark = random.choice([True,False])
            if shark :
                return s.Shark(indice,x,y,env,trace,self.sharkBreedTime,self.sharkStarveTime)
            else : 
                return f.Fish(indice,x,y,env,trace,self.fishBreedTime)