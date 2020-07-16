import pygame
from random import randint

pygame.init()

animCount = 0

W = 900
H = 700

x = 0
y = 0

sc = pygame.display.set_mode((W, H))

pygame.display.set_caption("Testik")

bg = pygame.image.load('sp_world/back_standart.jpg')

walkR = [pygame.image.load('sp_humans/Walk0000.png').convert_alpha(), pygame.image.load('sp_humans/Walk0001.png').convert_alpha(),
         pygame.image.load('sp_humans/Walk0002.png').convert_alpha(), pygame.image.load('sp_humans/Walk0003.png').convert_alpha(),
    pygame.image.load('sp_humans/Walk0004.png').convert_alpha(), pygame.image.load('sp_humans/Walk0005.png').convert_alpha(),
    pygame.image.load('sp_humans/Walk0006.png').convert_alpha(), pygame.image.load('sp_humans/Walk0007.png').convert_alpha()]
walkL = [pygame.image.load('sp_humans/WalkL0000.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0001.png').convert_alpha(),
         pygame.image.load('sp_humans/WalkL0002.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0003.png').convert_alpha(),
    pygame.image.load('sp_humans/WalkL0004.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0005.png').convert_alpha(),
    pygame.image.load('sp_humans/WalkL0006.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0007.png').convert_alpha()]

stay = [pygame.image.load('sp_humans/Stay10001.png').convert_alpha(), pygame.image.load('sp_humans/Stay10002.png').convert_alpha(), pygame.image.load('sp_humans/Stay10003.png').convert_alpha(),
        pygame.image.load('sp_humans/Stay10004.png').convert_alpha(), pygame.image.load('sp_humans/Stay10005.png').convert_alpha(),
    pygame.image.load('sp_humans/Stay10006.png').convert_alpha(), pygame.image.load('sp_humans/Stay10007.png').convert_alpha()]


motion = 'Stop'


# Пока закомментил вообще
def draw():
    global animCount

    # sc.blit(car1.image, car1.rect,walk,stay)
    pygame.time.delay(60)
    # Закомментил, из-за этого мигали анимации
    # pygame.display.update()


def draw_sprite(sprite, dest):
    sc.blit(sprite, dest)
    pygame.display.update()


while True:
    sc.blit(bg, (0, 0))

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
            draw_sprite(walkL[animCount], (x, y))
            animCount += 1
        else:
            animCount = 0
            draw_sprite(walkL[animCount], (x, y))
# if animCount + 1 >= 20:
# animCount=0

    elif motion == 'Right':
        x += 20
        if animCount <= len(walkR)-1:
            draw_sprite(walkR[animCount], (x, y))
            animCount += 1
        else:
            animCount = 0
            draw_sprite(walkR[animCount], (x, y))
    elif motion == 'Up':
        y -= 20
    elif motion == 'Down':
        y += 20
    elif motion == 'Stop':
        if animCount <= len(stay)-1:
            draw_sprite(stay[animCount], (x, y))
            animCount += 1
        else:
            animCount = 0
            draw_sprite(stay[animCount], (x, y))

    draw()
