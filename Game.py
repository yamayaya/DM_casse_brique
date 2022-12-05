import pyxel
import time
import math


from Brick import Brick
from Ball import Ball, ball
from Plato import Plato, plato

class Game:
    start_time = 0

    def __init__(self, name, x_start, y):
        self.name = name
        self.x_start = x_start
        self.y = y
        pyxel.init(self.x_start, self.y, title=name)
        Game.start_time = time.time()

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        plato.deplacement()
        Game.update_velocity_ball()
        ball.deplacement()

    def draw(self):
        pyxel.cls(0)
        if Plato.crossed_line_timer:
            Plato.draw_normal_bound()
        else:
            Plato.draw_crossed_bound()
        plato.draw_plato()
        ball.draw_ball()
        Brick.draw_bricks()

    @staticmethod
    def update_velocity_ball():
        present_time = time.time()
        ball.xv = round(ball.xv + (present_time - Game.start_time))
        ball.yv = round(ball.yv + (present_time - Game.start_time))
        Game.start_time = present_time









