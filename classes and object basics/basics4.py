import pygame
pygame.init()# initalisng window
#setting screen size
WIDTH = 1000
HEIGHT = 700

scr = pygame.display.set_mode((WIDTH, HEIGHT))
scr.fill("White")
pygame.display.update()
class rec():
    def __init__(self, colour, dimension):
        self.screen = scr
        self.colour = colour
        self.dimension = dimension
    def draw(self):
        self.drawrect = pygame.draw.rect(self.screen, self.colour, self.dimension)

rec1 = rec("Blue", (300, 200, 200, 150))
rec2 = rec("Green",(500, 400, 250, 100))
rec3 = rec("Yellow",(800, 300, 100, 200))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rec1.draw()
    rec2.draw()
    rec3.draw()
    pygame.display.update()
pygame.quit()