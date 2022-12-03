import pyxel
from Brick import Brick
from Ball import Ball
from Plato import Plato

pyxel.init(128, 128, title="Nuit du c0de")


plato = Plato(60, 120, 10, 4, 2)
ball = Ball(60, 60, 3, 1, 0, 3)

def update():

    plato.deplacement()
    ball.deplacement_from_start()

def draw():
    pyxel.cls(0)
    plato.draw_plato()
    ball.draw_ball()

pyxel.run(update, draw)
