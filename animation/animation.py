import pygame
import time

pygame.init()
WIDTH = 1000
HEIGHT = 1000

scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Celebrations")
halloween = pygame.image.load("halloween.jpg")
halloween = pygame.transform.scale(halloween, (WIDTH, HEIGHT))
easter = pygame.image.load("easter.jpg")
easter = pygame.transform.scale(easter, (WIDTH, HEIGHT))
chris = pygame.image.load("christmas.webp")
chris = pygame.transform.scale(chris, (WIDTH, HEIGHT))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# christmas
    fon = pygame.font.SysFont("Monospace", 55)
    fon2 = pygame.font.SysFont("Monospace",25)
    tex = fon.render("Merry Chrsitmas", 1, (180, 230, 200))
    smaltex = fon2.render("I hope the best for your wishes", 1, (1, 254, 200))
    scr.blit(chris, (0, 0))
    scr.blit(tex, (200, 150))
    scr.blit(smaltex, (200, 350))
    pygame.display.update()
    time.sleep(4)
# easter
    fon3 = pygame.font.SysFont("Display", 55)
    fon4 = pygame.font.SysFont("Display",25)
    eashead = fon3.render("Happy Easter", 1, (245, 25, 140))
    eassmall = fon4.render("Have an amazing easter", 1, (10, 230, 95))
    scr.blit(easter, (0, 0))
    scr.blit(eashead, (200, 200))
    scr.blit(eassmall, (350, 500))
    pygame.display.update()
    time.sleep(4)
# halloween
    fon5 = pygame.font.SysFont("Viking", 50)
    fon6 = pygame.font.SysFont("Viking", 25)
    hallhead = fon5.render("Spooky halloween", 1, (3,160, 255))
    hallsmall = fon6.render("hope you get all the sweets", 1, (255, 76, 234))
    scr.blit(halloween, (0, 0))
    scr.blit(hallhead, (300, 200))
    scr.blit(hallsmall, (300, 600))
    pygame.display.update()
    time.sleep(4)
    
    
    
    
    
    
    

pygame.quit()
    

    