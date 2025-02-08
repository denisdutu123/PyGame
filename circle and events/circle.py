import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600

scr = pygame.display.set_mode((WIDTH,HEIGHT))
# def colours
c1 = (255,255,255)
c2 = (196, 10, 78)
c3 = (11, 49, 201)
c4 = (210, 67, 90)
c5 = (65, 98, 199)
c6 = (89, 254, 253)
scr.fill(c3)
pygame.display.update()
class circ():
    def __init__ (self, color, pos , radius, width = 0):
        self.scr = scr
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
    def draw(self):
        pygame.draw.circle(self.scr, self.color, self.pos, self.radius, self.width)
    def grow(self, siz):
        self.radius+=siz
        pygame.draw.circle(self.scr, self.color, self.pos, self.radius, self.width)

#def objects
pygame.draw.circle(scr, c5, (300,200), 50, 20) 
pygame.display.update()
cir1 = circ(c2, (150, 300), 70, 40)
cir2 = circ(c1, (150, 300), 50, 30)
cir3 = circ(c6, (150, 300), 30, 20)
cir4 = circ(c4, (150, 300), 10, 15)


ru = True
while ru:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ru = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cir1.draw()
            cir2.draw()
            cir3.draw()
            cir4.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            cir1.grow(10)
            cir2.grow(20)
            cir3.grow(12)
            cir4.grow(11)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            cir5 = circ("grey", pos, 5)
            cir5.draw()
            pygame.display.update()

        
pygame.quit()

