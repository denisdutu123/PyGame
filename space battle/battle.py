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

bor = pygame.Rect(450, 0, 20, 700)
# blitting things on screen
def display():
    scr.blit(back, (0, 0))
    pygame.draw.rect(scr, white, bor)
    leftex = heafon.render("Health:" + str(lefhea), 1, red)
    scr.blit(leftex, (70, 70))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    display()
    pygame.display.update()
pygame.quit()
