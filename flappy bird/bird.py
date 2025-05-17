import pygame
import random
from pygame.locals import*

pygame.init()

scr = pygame.display.set_mode((864, 936))
pygame.display.set_caption("Flappy Bird")
fps = 60
clock = pygame.time.Clock()
# font
fon = pygame.font.SysFont("optic", 70)
# colours
col1 = (234, 169, 98)
# game variables
grouscr = 0
scrolspe = 6
fly = False
gaove = False
gap = 145
frepip = 1600
score = 0
paspip = False
lastpipe = pygame.time.get_ticks() - frepip
#loading images
background = pygame.image.load("bg.png")
ground = pygame.image.load("ground.png")
restart = pygame.image.load("restart.png")
# text on the screen
def text(tex, font, colo, xpos, ypos):
    tex = font.render(tex, 1, colo)
    scr.blit(tex, (xpos, ypos))

#reset function
#def restart():

class bird (pygame.sprite.Sprite):
    def __init__ (self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            birima = pygame.image.load(f"bird{i}.png")
            self.images.append(birima)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [xpos, ypos]
        self.vel = 0
        self.clicked = False

obj = bird(100, 450)
#group bird
group = pygame.sprite.Group()
group.add(obj)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.blit(background, (0, 0))
    pygame.display.update()
    
