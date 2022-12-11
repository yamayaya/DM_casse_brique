import pyxel
import time
import math
class Plato:
    crossed_line_timer = 0
    game_timer = 0
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
    def update_size_plato(self):
        self.size = ((self.x_start, self.y+self.dy-1), (self.x_start+self.dx/2, self.y), (self.x_start+3/2*self.dx, self.y), (self.x_start+2*self.dx, self.y+self.dy-1))
        return self.size
    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.update_size_plato()
            if (self.size[3][0] <= 124):
                self.x_start += 2
            else:
                pass
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.update_size_plato()
            if (self.size[0][0] >= 0):
                self.x_start -= 2
            else:
                pass
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.update_size_plato()
            if (self.size[1][1] < 124):
                pass
        elif pyxel.btn(pyxel.KEY_UP):
            self.update_size_plato()
            if (self.size[0][0] > 0):
                pass

        return self.x_start, self.y
    @staticmethod
    def draw_normal_bound():
        pyxel.line(0, plato.y + plato.dy / 2, 128, plato.y + plato.dy / 2, 13)

    @staticmethod
    def draw_crossed_bound():
        pyxel.line(0, plato.y + plato.dy / 2, 128, plato.y + plato.dy / 2, 8)

plato = Plato(60, 120, 10, 4, 2)


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








class Game:
    start_time = 0
    lives = 3
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
        Game.update_lives()

    def draw(self):
        pyxel.cls(0)
        if Game.lives <= 0:
            pyxel.text(50, 50, "GAME OVER", 8)
        elif len(Brick.bricks) == 0:
            pyxel.text(50, 50, "YOU WON", 11)
        else:

            if Plato.crossed_line_timer:
                Plato.draw_normal_bound()
            else:
                Plato.draw_crossed_bound()
            Game.draw_text_life()
            plato.draw_plato()
            ball.draw_ball()
            Brick.draw_bricks()

    @staticmethod
    def draw_text_life():
        pyxel.text(10, 5, "Lives:  ", 7)
        pyxel.text(35, 5, f"{Game.lives}", 7)

    @staticmethod
    def check_update_lives():
        if ball.deplacement_check_bounds_down() and (not (ball.deplacement_with_plato_up() or ball.deplacement_with_plato_left() or ball.deplacement_with_plato_right() )):
            return True
        else:
            return False

    @staticmethod
    def update_lives():
        if game.check_update_lives():
            Game.lives -=1
    @staticmethod
    def update_velocity_ball():
        present_time = time.time()
        ball.xv = round(ball.xv + (present_time - Game.start_time))
        ball.yv = round(ball.yv + (present_time - Game.start_time))
        Game.start_time = present_time

game = Game("Nuit du c0de",128, 128)
game.run()