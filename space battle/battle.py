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
wi = pygame.font.SysFont("monospace", 70)
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
lehit = pygame.USEREVENT+1
rihit = pygame.USEREVENT+2
            
        
# object creation 
le = ship(lef, 200, 350)
ri = ship(righ, 600, 350)
gro = pygame.sprite.Group()
gro.add(le)
gro.add(ri)

def collide():
    global lefhea, righea
    for n in lebul:
        if ri.rect.colliderect(n):
            righea-=1
            lebul.remove(n)
        elif n.x > 900:
            lebul.remove(n)
    for n in ribul:
        if le.rect.colliderect(n):
            lefhea-=1
            ribul.remove(n)
        elif n.x < 0:
            ribul.remove(n)
    for n1 in lebul:
        for n2 in ribul:
            if n1.colliderect(n2):
                lebul.remove(n1)
                ribul.remove(n2)
def endgame(txt):
    tex = wi.render(txt, 1, "blue")
    scr.blit(tex, (200, 150))
    pygame.display.update()
    pygame.time.delay(5000)
    
    
    

        
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
        if event.type == KEYDOWN:
            if event.key == K_1:
                bulll = pygame.Rect(le.rect.x + le.rect.width, le.rect.y + le.rect.height // 2, 10, 5)
                lebul.append(bulll)
            if event.key == K_2:
                bulll = pygame.Rect(ri.rect.x, ri.rect.y + ri.rect.height // 2, 10, 5)
                ribul.append(bulll)
                
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
    bullet()
    collide()
    if righea == 0:
        winnn = "Left ship wins"
        endgame(winnn)
        run = False
    if lefhea == 0:
        winnn = "Right ship wins"
        endgame(winnn)
        run = False
    
    
    
        
    pygame.display.update()
pygame.quit()
