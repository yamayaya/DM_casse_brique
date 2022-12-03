import pyxel

class Ball:
    def __init__(self, cx, cy, r, v, a, colour):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.size = ((self.cx-self.r, self.cy-self.r), (self.cx-self.r, self.cy+self.r), (self.cx+self.r, self.cy+self.r), (self.cx+self.r, self.cy-self.r))
        self.v = v
        self.a = a

        self.colour = colour

    def draw_ball(self):
        pyxel.circ(self.cx, self.cy, self.r, self.colour)

    def update_size_ball(self):
        self.size = ((self.cx-self.r, self.cy-self.r), (self.cx-self.r, self.cy+self.r), (self.cx+self.r, self.cy+self.r), (self.cx+self.r, self.cy-self.r))
        return self.size
    def deplacement_from_start(self):


        self.cy -= self.v
        self.cx += self.v
        self.update_size_ball()
        if (self.size[0][1] >= 0): #ВВЕРХ
            self.v = self.v
        else:
            self.bounce_from_up()

        if (self.size[0][0] >= 0): #ЛЕВЫЙ
            self.v = self.v
        else:
            self.bounce_from_left()

        if (self.size[2][0] <= 128): #ПРАВЫЙ
            self.v = self.v
        else:
            self.v = - self.v
            self.bounce_from_right()

        if (self.size[1][1] <= 128): #НИЗ
            self.v = self.v
        else:
            self.bounce_from_down()

    def bounce_from_up(self):
        self.cy += self.v
        self.cx += self.v

    def bounce_from_down(self):
        self.cy -= self.v
        self.cx += self.v

    def bounce_from_left(self):
        self.cy += self.v
        self.cx += self.v

    def bounce_from_right(self):
        self.cy -= self.v
        self.cx -= self.v

