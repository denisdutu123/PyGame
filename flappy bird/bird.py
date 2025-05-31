import pygame
import random
from pygame.locals import*

pygame.init()

scr = pygame.display.set_mode((864, 750))
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
    def update(self):
        if fly == True:
            self.vel +=0.7
            if self.vel > 7:
                self.vel = 7
            if self.rect.bottom < 750:
                self.rect.y += int(self.vel)
        if gaove == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel =- 10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # animating the bird
            flap = 6
            self.counter += 1
            if self.counter > flap:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]     
# class for pipes
class pipes(pygame.sprite.Sprite):
    def __init__ (self, xaxis, yaxis, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        #top or bottom pipe
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True )
            self.rect.bottomleft = [xaxis, yaxis - int(gap/2)]
        elif pos == -1:
            self.rect.topleft = [xaxis, yaxis + int(gap/2)]
    # update function
    def update(self):
        self.rect.x -= scrolspe
        if self.rect.right < 0:
            self.kill()
            
    
            
         
        
    
    
    

obj = bird(100, 450)
#group bird
group = pygame.sprite.Group()
group.add(obj)
# group pipe
groupip = pygame.sprite.Group()


run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and fly == False and gaove == False:
            fly = True
    scr.blit(background, (0, 0))
    
    scr.blit(ground, (grouscr, 675)) 
    group.draw(scr)
    groupip.draw(scr)
    group.update() 
    if fly == True and gaove == False:
        tim = pygame.time.get_ticks()
        if tim - lastpipe > frepip:
            piphei = random.randint(-150, 150)
            bottpip = pipes(864, 375 + piphei, -1)
            toppip = pipes(864, 375 + piphei, 1)
            groupip.add(bottpip)
            groupip.add(toppip)
            lastpip = tim
        groupip.update()
        
        grouscr -= scrolspe 
        if abs(grouscr) > 36:
            grouscr = 0
            
    pygame.display.update()
    


