import pygame
from pygame.locals import *
import os
import random

pygame.font.init()

WIDTH = 900
HEIGHT = 800
score = 0
fon = pygame.font.SysFont("Bold", 50)
scr = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.transform.scale(pygame.image.load("background.webp"), (900, 800))
tom = pygame.transform.scale(pygame.image.load("tom.png"), (100, 125))
jerry = pygame.transform.scale(pygame.image.load("jerry.png"), (100, 70))
tomspee = 6

class to(pygame.sprite.Sprite):
    def __init__(self, image, xaxis, yaxis):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = xaxis
        self.rect.y = yaxis
        

class jerr(pygame.sprite.Sprite):
    def __init__(self, image, xaxis, yaxis):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = xaxis
        self.rect.y = yaxis
        

    def position(self):
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0,400)

def collide():
    global score
    if tomob.rect.colliderect(jerryob):
        jerryob.position()
        score +=1 

def draw():
    scr.blit(background, (0, 0))
    tex1 = fon.render("score:"+str(score), 1, "White")
    scr.blit(tex1, (150, 100))
    
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
        tomob.rect.x-=5
    if ke [K_d]:
        tomob.rect.x+=5
    if ke [K_w]:
        tomob.rect.y-=5
    if ke [K_s]:
        tomob.rect.y+=5
    
    draw()
    grou.draw(scr)
    collide()
    pygame.display.update()

pygame.quit()




        
        
        
