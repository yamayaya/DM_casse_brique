import pyxel

class Brick:

    bricks = []
    def __init__(self, x_start, y, dx, dy, type, colour):
        self.x_start = x_start
        self.y = y
        self.dx = dx
        self.dy = dy
        self.type = type
        self.size = ((self.x_start, self.y), (self.x_start, self.y+self.dy), (self.x_start+self.dx, self.y+self.dx), (self.x_start+self.dy, self.y))
        self.colour = colour
        Brick.bricks.append(self)


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
    @staticmethod
    def draw_bricks():
        for i in Brick.bricks:
            i.draw_brick()

[Brick(5+15*i, 20, 12, 7, 3, 8) for i in range(8)]
[Brick(10+15*i, 40, 12, 7, 3, 8) for i in range(7)]