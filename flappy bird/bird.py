import pygame
import random
from pygame.locals import*

pygame.init()

scr = pygame.display.set_mode((864, 700))
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
gap = 200
frepip = 1500
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
            
            
class button():
    def __init__ (self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        scr.blit(self.image, (self.rect.x, self.rect.y))
        return action
def reset ():
    groupip.empty()
    obj.rect.x = 100
    obj.rect.y = 450
    score = 0
    return score

# button object
butto = button(432, 375, restart)

            


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
    # updating score
    if len(groupip) > 0:
        
        if group.sprites()[0].rect.left > groupip.sprites()[0].rect.left\
            and group.sprites()[0].rect.right < groupip.sprites()[0].rect.right\
                and paspip == False:
                    paspip = True
                    
        if paspip == True:
            if group.sprites()[0].rect.left > groupip.sprites()[0].rect.right:
                score +=1
                paspip = False
    if pygame.sprite.groupcollide(group, groupip, False, False) or obj.rect.top < 0 :
        gaove = True
        fly = False
    if obj.rect.bottom >= 700:
        gaove = True
        fly = False
    
        
        
        
        
    text(str(score), fon, "Red", 100, 75)
    scr.blit(ground, (grouscr, 675)) 
    group.draw(scr)
    groupip.draw(scr)
    group.update() 
    if obj.rect.bottom >= 750:
        gaove = True
        fly = False
    if fly == True and gaove == False:
        tim = pygame.time.get_ticks()
        if tim - lastpipe > frepip:
            piphei = random.randint(-150, 150)
            bottpip = pipes(864, 375 + piphei, -1)
            toppip = pipes(864, 375 + piphei, 1)
            groupip.add(bottpip)
            groupip.add(toppip)
            lastpipe = tim
        groupip.update()
        
        grouscr -= scrolspe 
        if abs(grouscr) > 36:
            grouscr = 0
    if gaove == True:
        if butto.draw():
            gaove = False
            score = reset()
    pygame.display.update()
    
