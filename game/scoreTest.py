import sys
sys.path.append('..')

import Avatar as a
from core import Environnement as e


env = e.Environnement(10, 10)
avatar = a.Avatar(5,5,env)
env.ajouteAgent(avatar)

avatar.calculeScore()
for line in env.score :
    print(line)