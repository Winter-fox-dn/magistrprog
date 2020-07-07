
from Window_Dialog import pygame
import Window_Dialog

import readfile
pygame.init()

Width = 900
Height = 700



sc = pygame.display.set_mode((Width, Height))
sc.fill((0, 0, 0))



#sprt = ('slav_1.jpg','slav_2.jpg','slav_3.jpg','slav_4.jpg','slav_5.jpg','slav_6.jpg')
sprt = ('slav_2.jpg','slav.png')

sprt_surf = []

slavia = pygame.sprite.Group()
#Рисунки и их координаты
for i in range(len(sprt)):
    sq = Window_Dialog.Pictures('sp_humans/'+sprt[i], 600, 700, slavia)
    sq.moveLeft();
    sq.moveLeft();
    sprt_surf.append(sq)


#Задний фон
bacpick = Window_Dialog.Pictures('sp_world/back_standart.jpg', Width, Height)
print(bacpick.path)

#отрисовка окна с рисунками
window = Window_Dialog.DialogWindow(Width, Height, bacpick, sprt_surf)
sc.blit(window.drawDialogWind1(),(0,0))

#        
r = readfile.TextRead('proba').readScene()
r.reverse()
print(r)

font_title = pygame.font.SysFont(None, 20)

font_text = pygame.font.SysFont(None, 20)


while 1:
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            exit()
            
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
               pass
 
    pygame.display.update()
 
    pygame.time.delay(30)

