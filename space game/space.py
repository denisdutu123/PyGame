import pygame
from pygame.locals import*
from time import*

pygame.init()
# set screen size
scr = pygame.display.set_mode((700,700))
xpos = 350
ypos = 100
ke = [False, False, False, False]
#loading images
bac = pygame.image.load("background.jpg")
bac = pygame.transform.scale(bac, (700, 700))
ship = pygame.image.load("ufo.png")
ship = pygame.transform.scale(ship, (200, 150))

while ypos < 700:
    scr.blit(bac,(0, 0))
    scr.blit(ship, (xpos, ypos))
    pygame.display.update()
    #quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                ke[0] = True
            if event.key == K_DOWN:
                ke[2] = True
            if event.key == K_LEFT:
                ke[1] = True
            if event.key == K_RIGHT:
                ke[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                ke[0] = False
            if event.key == K_DOWN:
                ke[2] = False
            if event.key == K_LEFT:
                ke[1] = False
            if event.key == K_RIGHT:
                ke[3] = False
    if ke[0]:
        if ypos > 150:
            ypos-=5
    if ke[2]:
        if ypos < 550:
            ypos+=5
    if ke[1]:
        if xpos > 200:
            xpos-=5
    if ke[3]:
        if xpos < 500:
            xpos+=5
                
    ypos+=3
    sleep(0.05)

print("GAME OVER")
            
            