import pyxel


class Plato:
    def __init__(self, x_start, y, dx, dy, colour):
        self.x_start = x_start
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = ((self.x_start, self.y+self.dy-1), (self.x_start+self.dx/2, self.y), (self.x_start+3/2*self.dx, self.y), (self.x_start+2*self.dx, self.y+self.dy-1))
        self.colour = colour

    def draw_plato(self):
        pyxel.tri(self.x_start, self.y+self.dy-1, self.x_start+self.dx/2, self.y+self.dy-1, self.x_start+self.dx/2, self.y, self.colour)
        pyxel.rect(self.x_start+self.dx/2, self.y, self.dx, self.dy, self.colour)
        pyxel.tri(self.x_start+3/2*self.dx, self.y, self.x_start+3/2*self.dx, self.y+self.dy-1, self.x_start+2*self.dx, self.y+self.dy-1, self.colour)
        #ТРАПЕЦИЯ

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (self.size[3][0] <= 120):
                self.x_start += 1
            else:
                pass
        elif pyxel.btn(pyxel.KEY_LEFT):
            if (self.size[0][0] >= 0):
                self.x_start -= 1
            else:
                pass
        elif pyxel.btn(pyxel.KEY_DOWN):
            if (self.size[1][1] < 120):
                pass
        elif pyxel.btn(pyxel.KEY_UP):
            if (self.size[0][0] > 0):
                pass

        return self.x_start, self.y