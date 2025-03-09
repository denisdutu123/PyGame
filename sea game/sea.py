import pygame
from pygame.locals import*
from time import*

pygame.init()
scr = pygame.display.set_mode((700,700))
xpos = 350
ypos = 100
back = pygame.image.load("background.jpg")
back = pygame.transform.scale(back, (700, 700))
ani = pygame.image.load("shark.png")
ani = pygame.transform.scale(ani, (200, 150))
ke = [False, False, False, False]
while ypos < 700:
    scr.blit(back,(0, 0))
    scr.blit(ani, (xpos, ypos))
    pygame.display.update()
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
                
    ypos+=4
    sleep(0.75)

print("YA DEAD")
            
            