import time
import math
import pyxel

from Brick import Brick
from Plato import Plato, plato


class Ball:
    def __init__(self, cx, cy, r, xv, yv, a, colour):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.size = ((self.cx-self.r, self.cy-self.r), (self.cx-self.r, self.cy+self.r), (self.cx+self.r, self.cy+self.r), (self.cx+self.r, self.cy-self.r))
        self.xv = xv
        self.yv = yv
        self.a = a

        self.colour = colour

    def draw_ball(self):
        pyxel.circ(self.cx, self.cy, self.r, self.colour)

    def update_size_ball(self):
        self.size = ((self.cx-self.r, self.cy-self.r), (self.cx-self.r, self.cy+self.r), (self.cx+self.r, self.cy+self.r), (self.cx+self.r, self.cy-self.r))
        return self.size

    def deplacement(self):
        self.cy += self.yv
        self.cx += self.xv
        self.update_size_ball()

        if self.deplacement_with_plato_up():
            self.yv = -self.yv

        if self.deplacement_with_plato_left():
            self.xv = -self.xv

        if self.deplacement_with_plato_right():
            self.xv = -self.xv

        for i in Brick.bricks:
            if self.deplacement_with_brick_up(i):
                self.yv = -self.yv
                i.type -= 1
                if i.type == 0:
                    Brick.bricks.remove(i)

            if self.deplacement_with_brick_left(i):
                self.xv = -self.xv
                i.type -= 1
                if i.type == 0:
                    Brick.bricks.remove(i)

            if self.deplacement_with_brick_right(i):
                self.xv = -self.xv
                i.type -= 1
                if i.type == 0:
                    Brick.bricks.remove(i)

            if self.deplacement_with_brick_down(i):
                self.yv = -self.yv
                i.type -= 1
                if i.type == 0:
                    Brick.bricks.remove(i)

        if self.deplacement_check_bounds_up() or self.deplacement_check_bounds_down(): #ВВЕРХ И НИЗ
            Plato.draw_crossed_bound()
            self.yv = -self.yv

        if self.deplacement_check_bounds_left_right(): #ЛЕВЫЙ И ПРАВЫЙ
            self.xv = -self.xv

    def deplacement_check_bounds_up(self):
        if (self.size[0][1] <= 0):  # ВВЕРХ И НИЗ
            Plato.crossed_line_timer = 30
            return True
        else:
            Plato.crossed_line_timer -= 1
            return False
    def deplacement_check_bounds_down(self):
        if (self.size[1][1] >= plato.y + plato.dy / 2):  # ВВЕРХ И НИЗ
            Plato.crossed_line_timer = 30
            return True
        else:
            Plato.crossed_line_timer -= 1
            return False
    def deplacement_check_bounds_left_right(self):
        if (self.size[0][0] <= 0 or self.size[2][0] >= 128): #ЛЕВЫЙ И ПРАВЫЙ
            return True
        else:
            return False
    def deplacement_with_plato_up(self):
        top = [(i, plato.y) for i in range(plato.x_start, plato.x_start + 2 * plato.dx)]
        flag = False
        for cood in top:
            if self.size[2][0] <= cood[0] and self.size[1][1] >= cood[1]:
                flag = True
        return flag

    def deplacement_with_plato_left(self):
        left = [(plato.x_start, i) for i in range(plato.y, plato.y + plato.dy - 1)]
        flag = False
        for cood in left:
            if self.size[2][0] >= cood[0] and self.size[0][1] >= cood[1]:
                flag = True
        return  flag

    def deplacement_with_plato_right(self):
        right = [(plato.x_start + 2 * plato.dx, i) for i in range(plato.y, plato.y + plato.dy - 1)]
        flag = False
        for cood in right:
            if self.size[0][0] <= cood[0] and self.size[0][1] >= cood[1]:
                flag = True
        return flag

    def deplacement_with_brick_up(self, brick):
        top = [(i, brick.y) for i in range(brick.x_start, brick.x_start + brick.dx)]
        flag = False
        for cood in top:
            if self.size[2][0] == cood[0] and self.size[1][1] == cood[1]:
                flag = True
        return flag

    def deplacement_with_brick_left(self, brick):
        left = [(brick.x_start, i) for i in range(brick.y, brick.y + brick.dy)]
        flag = False
        for cood in left:
            if self.size[2][0] == cood[0] and self.size[0][1] == cood[1]:
                flag = True
        return flag

    def deplacement_with_brick_right(self, brick):
        right = [(brick.x_start + brick.dx, i) for i in range(brick.y, brick.y + brick.dy)]
        flag = False
        for cood in right:
            if self.size[0][0] == cood[0] and self.size[0][1] == cood[1]:
                flag = True
        return flag

    def deplacement_with_brick_down(self, brick):
        down = [(i, brick.y + brick.dy) for i in range(brick.x_start, brick.x_start + brick.dx)]
        flag = False
        for cood in down:
            if self.size[0][0] == cood[0] and self.size[0][1] == cood[1]:
                flag = True
        return flag

ball = Ball(plato.x_start+3/2*plato.dx, 60, 2, 1, 1, 0, 3)