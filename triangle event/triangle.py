import pygame
pygame.init()

WIDTH = 750
HEIGHT = 600

scr = pygame.display.set_mode((WIDTH,HEIGHT))

re1 = (193,201,93)
re2 = (233,245,2)
re3 = (45,109,200)
re4 = (255,254,253)
re5 = (99,156,56)

scr.fill(re4)
pygame.display.update()
class rectan():
    def __init__ (self, color, pos, height, width = 0):
        self.scr = scr
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.rect(self.scr, self.color, (*self.pos, self.height, self.height), self.width)
    def grow(self, siz):
        self.height+=siz
        pygame.draw.rect(self.scr, self.color, (*self.pos, self.height, self.height), self.width)
#pygame.draw.rect(scr, re2, (400, 300), 60)
pygame.display.update()
recta1 = rectan(re1, (250,300), 50)
recta2 = rectan(re3, (250,300), 35)
recta3 = rectan(re5, (250,300), 25)

ru = True
while ru:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ru = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            recta1.draw()
            recta2.draw()
            recta3.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            recta1.grow(25)
            recta2.grow(21)
            recta3.grow(15)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            recta4 = rectan("Black", pos, 15)
            recta4.draw()
            pygame.display.update()
pygame.quit()