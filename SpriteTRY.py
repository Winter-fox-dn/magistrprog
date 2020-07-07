import pygame
from random import randint

pygame.init()

animCount = 0

W = 900
H = 700

class Car(pygame.sprite.Sprite):
    def __init__(self, x, filename, wk_ls = 0, st_ls = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sp_humans/'+filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x,0))
        self.wk_ls = wk_ls
        self.st_ls = st_ls


x = 0
y = 0

sc = pygame.display.set_mode((W,H))

car1 = Car(300, 'Walk0000.png')

pygame.display.set_caption("Testik")

bg = pygame.image.load('sp_world/back_standart.jpg')

walkR = [pygame.image.load('sp_humans/Walk0000.png').convert_alpha(),pygame.image.load('sp_humans/Walk0001.png').convert_alpha(),
        pygame.image.load('sp_humans/Walk0002.png').convert_alpha(),pygame.image.load('sp_humans/Walk0003.png').convert_alpha(),
        pygame.image.load('sp_humans/Walk0004.png').convert_alpha(),pygame.image.load('sp_humans/Walk0005.png').convert_alpha(),
        pygame.image.load('sp_humans/Walk0006.png').convert_alpha(),pygame.image.load('sp_humans/Walk0007.png').convert_alpha()]
walkL = [pygame.image.load('sp_humans/WalkL0000.png').convert_alpha(),pygame.image.load('sp_humans/WalkL0001.png').convert_alpha(),
        pygame.image.load('sp_humans/WalkL0002.png').convert_alpha(),pygame.image.load('sp_humans/WalkL0003.png').convert_alpha(),
        pygame.image.load('sp_humans/WalkL0004.png').convert_alpha(),pygame.image.load('sp_humans/WalkL0005.png').convert_alpha(),
        pygame.image.load('sp_humans/WalkL0006.png').convert_alpha(),pygame.image.load('sp_humans/WalkL0007.png').convert_alpha()]

stay =[ pygame.image.load('sp_humans/Stay10001.png').convert_alpha(),pygame.image.load('sp_humans/Stay10002.png').convert_alpha(),pygame.image.load('sp_humans/Stay10003.png').convert_alpha(),
       pygame.image.load('sp_humans/Stay10004.png').convert_alpha(),pygame.image.load('sp_humans/Stay10005.png').convert_alpha(),
       pygame.image.load('sp_humans/Stay10006.png').convert_alpha(),pygame.image.load('sp_humans/Stay10007.png').convert_alpha()]




motion = 'Stop'

def draw():
    global animCount
    
    #sc.blit(car1.image, car1.rect,walk,stay)
    pygame.time.delay(60)
    pygame.display.update()

     
while 1:
    sc.blit(bg,(0,0))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = 'Left'
            elif i.key == pygame.K_RIGHT:
                motion = 'Right'
            elif i.key == pygame.K_UP:
                motion = 'Up'
            elif i.key == pygame.K_DOWN:
                motion = 'Down'
        else:
            motion = 'Stop'
            
            
 
    if motion == 'Left':
        x -= 20
        if animCount <= len(walkL)-1:
            sc.blit(walkL[animCount], (x,y))
            animCount +=1
        else:
            animCount=0
##        if animCount + 1 >= 20:
##            animCount=0
        
    elif motion == 'Right':
        x += 20
        if animCount <= len(walkR)-1:
            sc.blit(walkR[animCount], (x,y))
            animCount +=1
        else:
            animCount=0
    elif motion == 'Up':
        y -= 20
    elif motion == 'Down':
        y += 20 
    elif motion == 'Stop':
        if animCount <= len(stay)-1:
            sc.blit(stay[animCount], (x,y))
            animCount +=1
        else:
            animCount=0
    
    draw()
