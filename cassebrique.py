import Pyxel 
pyxel.init(128, 128, title="Nuit du c0de")
def vaisseau_deplacement(x):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    return x
    
