import pgzrun
import random

TITLE = "Bouncy ball"

WIDTH = 700
HEIGHT = 650

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

col = r,g,b
grav = 2000.0

class ball():
    def __init__ (self, initial_x, initial_y):
        self.initial_x = initial_x
        self.inital_y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 60
    def draw(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        col = r,g,b
        pos = (self.initial_x, self.inital_y)
        screen.draw.filled_circle(pos, self.radius, col)
ba1 = ball(400, 350)
ba2 = ball(300,250)
ba3 = ball(390, 400)
obj = [ba1, ba2, ba3]
def draw():
    for i in obj:
        i.draw()
def update(ti):
    global obj
    pass
    # applying constant acceleration formula
    for i in obj:
        uy = i.vy
        i.vy += grav * ti
        i.inital_y += (uy + i.vy) * 0.5 * ti
        # detecting and handling bounce
        if i.inital_y > 590:
            i.inital_y = 590
            i.vy = -i.vy * 0.9
        i.initial_x += i.vx * ti
        if i.initial_x > 640 or i.initial_x < 60:
            i.vx = -i.vx
def on_key_down(key):
    if key == keys.SPACE:
        ba1.vy = -350
        ba2.vy = -300
        ba3.vy = -325

pgzrun.go()


        