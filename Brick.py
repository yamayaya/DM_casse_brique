import pyxel

from Ball import Ball
from Plato import Plato

class Brick:
    def __init__(self, x_start, y, dx, dy, type, colour):
        self.x_start = x_start
        self.y = y
        self.dx = dx
        self.dy = dy
        self.type = type
        self.size = ((self.x_start, self.y), (self.x_start, self.y+self.dy), (self.x_start+self.dx, self.y+self.dx), (self.x_start+self.dy, self.y))
        self.colour = colour


    def update_size_brick(self):
        self.size = ((self.x_start, self.y), (self.x_start, self.y+self.dy), (self.x_start+self.dx, self.y+self.dx), (self.x_start+self.dy, self.y))
        return self.size

    def draw_brick(self):
        if self.type  == 3:
            pyxel.rect(self.x_start, self.y, self.dx, self.dy, self.colour)
            pyxel.line(self.x_start, self.y, self.x_start + self.dx - 1, self.y + self.dy - 1, self.colour + 1)
            pyxel.line(self.x_start, self.y+self.dy - 1, self.x_start + self.dx - 1, self.y, self.colour + 1)
        elif self.type == 2:
            pyxel.rect(self.x_start, self.y, self.dx, self.dy, self.colour)
            pyxel.line(self.x_start, self.y, self.x_start + self.dx - 1, self.y + self.dy - 1, self.colour + 1)
        elif self.type == 1:
            pyxel.rect(self.x_start, self.y, self.dx, self.dy, self.colour)

brick = Brick(20, 20, 10, 5, 3, 8)