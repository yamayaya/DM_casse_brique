import pyxel
from Plato import plato
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

        if (self.size[0][1] <= 0): #ВВЕРХ
            self.yv = -self.yv

        if (self.size[0][0] <= 0): #ЛЕВЫЙ
            self.xv = -self.xv

        if (self.size[2][0] >= 128): #ПРАВЫЙ
            self.xv = -self.xv

        if (self.size[1][1] >= 128): #НИЗ
            self.yv = -self.yv


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

ball = Ball(30, 60, 3, 1, 1, 0, 3)