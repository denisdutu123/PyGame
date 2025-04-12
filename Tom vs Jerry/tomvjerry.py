
        import pygame
from pygame.locals import *
import os
import random

pygame.font.init()

WIDTH = 900
HEIGHT = 800
score = 0
scr = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.transform.scale(pygame.image.load("background.webp"), (900, 800))
tom = pygame.image.load("tom.png")
jerry = pygame.image.load("jerry.png")
tomspee = 6

class to(pygame.sprite.Sprite):
    def __init__(self, image, xaxis, yaxis):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = xaxis
        self.rect.y = yaxis

class jerr(pygame.sprite.Sprite):
    def __init__(self, image, xaxis, yaxis):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = xaxis
        self.rect.y = yaxis
        

    def position(self):
        self.rect.pos = random.randint(0, 800), random.randint(0, 400) 

def collide():
    if tom.rect.colliderect():
        score =+1
    else:
        score = 0

def draw():
    scr.blit(background, (0, 0))
    #scr.draw.text("GAME OVER, score:"+str(score), center = (450, 400), fontsize = 50)
#quit function
run = True
tomob = to(tom, 500, 350)
jerryob = jerr(jerry, 400, 200)
grou = pygame.sprite.Group()
grou.add(tomob)
grou.add(jerryob)

clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# moveme for tom
    ke = pygame.key.get_pressed()
    if ke [K_a]:
        tomob.x-=5
    if ke [K_d]:
        tomob.x+=5
    if ke [K_w]:
        tomob.y+=5
    if ke [K_s]:
        tomob.y-=5
    
    draw()
    grou.draw(scr)
    #collide()
    pygame.display.update()

pygame.quit()




        
        
        
