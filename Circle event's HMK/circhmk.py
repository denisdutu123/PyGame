import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
scr = pygame.display.set_mode((WIDTH,HEIGHT))
scr.fill("green")
pygame.display.update()
class circ():
    def __init__(self, color, x, y, radius):
        self.scr = scr
        self.color = color
        self.pos = (x, y)
        self.radius = radius
    def draw(self):
        pygame.draw.circle(self.scr, self.color,self.pos,self.radius)
# object creation
cir1 = circ("Blue", 250,75, 40)
cir2 = circ("Yellow", 321, 56, 60)
cir3 = circ("orange", 350,200, 30)
cir4 = circ("Pink", 50, 169, 56)
cir5 = circ("Purple", 410, 312, 91)

ru = True
while ru:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ru = False
    cir1.draw()
    cir2.draw()
    cir3.draw()
    cir4.draw()
    cir5.draw()
    pygame.display.update()
pygame.quit()