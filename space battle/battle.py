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
spee = 7
bulspe = 9
maxbul = 5
lebul = []
ribul = []
heafon = pygame.font.SysFont("pacifico", 40)
#colours
red = (255, 0, 0)
white = (255, 255, 255)
lorange = (255, 165, 0)
ryellow = (255, 255, 0)
# class for spaceships
class ship(pygame.sprite.Sprite):
    def __init__ (self, image, xaxis, yaxis):
        super().__init__()
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = xaxis
        self.rect.y = yaxis
    def horizontal(self, spe, p1):
        self.rect.x+=spe
        if p1 == 1:
            if self.rect.left <= 0 or self.rect.right >= bor.left:
                self.rect.move_ip(-spe, 0)
        if p1 == 2:
            if self.rect.left <= bor.right or self.rect.right >= 900:
                self.rect.move_ip(-spe, 0)       
    def vertical(self, spe):
        self.rect.move_ip(0, spe)
        if self.rect.top <= 0 or self.rect.bottom >= 700:
            self.rect.move_ip(0, -spe)

#drawing bullets
def bullet():
    for i in lebul:
        pygame.draw.rect(scr, lorange, i)
        i.x+=bulspe
    for i in ribul:
        pygame.draw.rect(scr, ryellow, i)
        i.x-=bulspe
        
        
            
        
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
    ke = pygame.key.get_pressed()
    # player 1
    if ke [K_a]:
        le.horizontal(-spee, 1)
    if ke [K_d]:
        le.horizontal(spee, 1)
    if ke [K_w]:
        le.vertical(-spee)
    if ke [K_s]:
        le.vertical(spee)
    #player 2
    if ke [K_LEFT]:
        ri.horizontal(-spee, 2)
    if ke [K_RIGHT]:
        ri.horizontal(spee, 2)
    if ke [K_UP]:
        ri.vertical(-spee)
    if ke [K_DOWN]:
        ri.vertical(spee)
    
    display()
    gro.draw(scr)
    pygame.display.update()
pygame.quit()
