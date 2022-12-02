import pyxel

from Classes.Ball import Ball
from Classes.Plato import Plato

pyxel.init(128, 128, title="Nuit du c0de")


plato = Plato(60, 120, 20, 4, 2)
ball = Ball(30, 30, 5, 8)

def update():

    global vaisseau_x, vaisseau_y
    vaisseau_x, vaisseau_y = plato.deplacement()


def draw():
    pyxel.cls(0)
    plato.draw_plato()
    ball.draw_ball()

pyxel.run(update, draw)
