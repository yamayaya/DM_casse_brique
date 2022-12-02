import pyxel

class Ball:
    def __init__(self, cx, cy, r, colour):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.size = (cx, cy, r)
        self.colour = colour

    def draw_ball(self):
        pyxel.circ(self.cx, self.cy, self.r, self.colour)

    def deplacement(self):
        # Движение
        pass