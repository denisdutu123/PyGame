import pygame
from pygame.locals import *
import os

pygame.font.init()

WIDTH = 900
HEIGHT = 700

scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" The Battle")
back = pygame.transform.scale(pygame.image.load("background.jpg"), (900, 700))
lef = pygame.image.load("first.png")
righ = pygame.image.load("second.png")
lefhea = 10
righea = 10
heafon = pygame.font.SysFont("pacifico", 40)
#colours
red = (255, 0, 0)
white = (255, 255, 255)
lorange = (255, 165, 0)
ryellow = (255, 255, 0)
# class for spaceships
class ship(pygame.sprite.Sprite):
    def __inti__ (self, image, xaxis, yaxis):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = xaxis
        self.rect.y = yaxis
# object creation 
le = ship(lef, 200, 350)
ri = ship(righ, 600, 350)
gro = pygame.sprite.Group()
gro.add(le)
gro.add(ri)

        
bor = pygame.Rect(450, 0, 20, 700)
# blitting things on screen
def display():
    scr.blit(back, (0, 0))
    pygame.draw.rect(scr, white, bor)
    leftex = heafon.render("Health:" + str(lefhea), 1, red)
    scr.blit(leftex, (70, 70))
    rigtex = heafon.render("Health:" + str(righea), 2, red)
    scr.blit(rigtex, (750, 70))
# quit function 
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    display()
    gro.draw(scr)
    pygame.display.update()
pygame.quit()
