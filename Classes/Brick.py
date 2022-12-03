import pyxel

from Classes.Ball import Ball
from Classes.Plato import Plato

class Brick:
    def __init__(self, x_start, y, dx, dy, colour):
        self.x_start = x_start
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = ((self.x_start, self.y), (self.x_start, self.y+self.dy), (self.x_start+self.dx, self.y+self.dx), (self.x_start+self.dy, self.y))
        self.colour = colour


    def update_size_brick(self):
        self.size = ((self.x_start, self.y), (self.x_start, self.y+self.dy), (self.x_start+self.dx, self.y+self.dx), (self.x_start+self.dy, self.y))
        return self.size
