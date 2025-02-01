import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600

scr = pygame.display.set_mode((WIDTH,HEIGHT))
# def colours
c1 = (255,255,255)
c2 = (196, 10, 78)
c3 = (11, 49, 201)
c4 = (210, 67, 90)
c5 = (65, 98, 199)
c6 = (89, 254, 253)
scr.fill(c5)
pygame.display.update()

ru = True
while ru:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ru = False
pygame.quit()

