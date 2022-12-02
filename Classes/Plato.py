import pyxel


class Plato:
    def __init__(self, x, y, dx, dy, colour):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = (x, y, x+dx, y+dy)
        self.colour = colour

    def draw_plato(self):
        pyxel.rect(self.x, self.y, self.dx, self.dy, self.colour)

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (self.x +self.dx/2 <= 120):
                self.x += 1
            else:
                pass
        elif pyxel.btn(pyxel.KEY_LEFT):
            if (self.x >= 0):
                self.x -= 1
            else:
                pass
        elif pyxel.btn(pyxel.KEY_DOWN):
            if (self.y < 120):
                pass
        elif pyxel.btn(pyxel.KEY_UP):
            if (self.y > 0):
                pass

        return self.x, self.y