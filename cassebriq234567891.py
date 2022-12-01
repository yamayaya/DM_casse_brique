import pyxel

pyxel.init(128, 128, title="Nuit du c0de")

vaisseau_x = 60
vaisseau_y = 120

def vaisseau_deplacement(x):


    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1

    return x


def update():

    global vaisseau_x, vaisseau_y
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)


def draw():
    pyxel.cls(0)
    pyxel.rect(vaisseau_x, vaisseau_y, 20, 4, 1)

pyxel.run(update, draw)
