import pygame
import random

pygame.font.init()

WIDTH = 900
HEIGHT = 700

scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tom vs Jerry")
back = pygame.transform.scale(pygame.image.load("background.webp"), (900, 700))
tom = pygame.image.load("tom.png")
jerry = pygame.image.load("jerry.png")


run = True
clock = pygame.time.Clock()
while run:
    clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    ke = pygame.key.get_pressed()
    scr.blit(back, (0, 0))
    scr.blit(tom, (450, 300))
    scr.blit(jerry, (200, 500))
    pygame.display.update()

pygame.quit()
        