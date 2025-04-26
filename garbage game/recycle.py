import pygame
import time
import random
from pygame.locals import*

WIDTH = 1200
HEIGHT = 800

pygame.init()
pygame.display.set_caption("RECYCLE GAME")
scr = pygame.display.set_mode((WIDTH, HEIGHT))

# changing background
def background(image):
    back = pygame.image.load(image)
    back = pygame.transform.scale(back, (WIDTH, HEIGHT))
    scr.blit(back, (0, 0))
    
# class for bin
class bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load("bin.png")), (100, 125))
        self.rect = self.image.get_rect()
        
# bin object
bi = bin()

grou = pygame.sprite.Group()
grou.add(bi)


        
    
# main loop function
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # setting background
    background("background.jpg")
    grou.draw(scr)
    pygame.display.update()
    









pygame.quit()
    