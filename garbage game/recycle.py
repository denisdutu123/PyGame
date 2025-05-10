import pygame
import time
import random
from pygame.locals import*

WIDTH = 1200
HEIGHT = 800

colo = (123, 67, 234)
scor = 0
clock = pygame.time.Clock()
statim = time.time()
pygame.init()
pygame.display.set_caption("RECYCLE GAME")
scr = pygame.display.set_mode((WIDTH, HEIGHT))
fon = pygame.font.SysFont("Opitc", 40)
tex = fon.render("Score:" + str(scor), True, colo)
textim = fon.render

# changing background
def background(image):
    back = pygame.image.load(image)
    back = pygame.transform.scale(back, (WIDTH, HEIGHT))
    scr.blit(back, (0, 0))
    
# class for bin
class bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load("bin.png")), (100, 125))
        self.rect = self.image.get_rect()
        
class recycable(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load(image)), (75, 75))
        self.rect = self.image.get_rect()
class nonrecycable(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load("plastic.png")), (100, 75))
        self.rect = self.image.get_rect()

#list of recycable items
recy = ["wood.png", "pencil.png", "paper.png"]
#creating groups
recycab = pygame.sprite.Group()
nonrecycab = pygame.sprite.Group()

# bin object
bi = bin()

grou = pygame.sprite.Group()
grou.add(bi)

#non - recycable object creation
for i in range(10):
    plas = nonrecycable()
    plas.rect.x = random.randint(150, 1050)
    plas.rect.y = random.randint(100, 700)
    nonrecycab.add(plas)
    grou.add(plas)

#recycable object creation
for i in range(25):
    imag = recycable(random.choice(recy))
    imag.rect.x = random.randint(150, 1050)
    imag.rect.y = random.randint(100, 700)
    recycab.add(imag)
    grou.add(imag)
    


        

        
# main loop function
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    total = time.time() - statim
    if total >= 30:
        if scor > 6:
            background("win.webp")
        else:
            background("lost.jpeg")
        scr.blit(tex, (600, 400))
    else:
        
               
        # setting background
        background("background.jpg")
        timtex = fon.render("Time Left:" + str(30 - int(total)), True, "Black")
        scr.blit(timtex, (1000, 60))
        grou.draw(scr)
        pygame.display.update()
        ke = pygame.key.get_pressed()
        if ke [K_w]:
            bi.rect.y -=5
        if ke [K_s]:
            bi.rect.y +=5
        if ke [K_a]:
            bi.rect.x -=5
        if ke [K_d]:
            bi.rect.x +=5
        #collison
        recyite = pygame.sprite.spritecollide(bi, recycab, True)
        nonrecyite = pygame.sprite.spritecollide(bi, nonrecycab, True)
        
        for i in recyite:
            scor +=1
            tex = fon.render("Score:" + str(scor), True, colo)
        for n in nonrecyite:
            scor -=2
            tex = fon.render("Score:" + str(scor), True, colo)
            
        scr.blit(tex, (130, 100))
    
    
    pygame.display.update()








pygame.quit()
    
