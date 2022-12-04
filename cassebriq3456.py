import pyxel
from Brick import Brick, brick
from Ball import Ball, ball
from Plato import Plato, plato

pyxel.init(128, 128, title="Nuit du c0de")

def update():

    plato.deplacement()
    ball.deplacement()

def draw():
    pyxel.cls(0)
    plato.draw_plato()
    ball.draw_ball()
    brick.draw_brick()

pyxel.run(update, draw)
