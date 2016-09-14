from particules import Bille as b

class BilleCreator(BilleCreator):
    """docstring for BilleCreator"""
    def __init__(self):
        super(BilleCreator, self).__init__()

    def create(indice,x,y,env,trace) :
        return b.Bille(indice,x,y,env,trace)
        