#Импорт класса отрисовывающего окна
from Window_Dialog import pygame
import Window_Dialog
#Импорт класса ГГ
import CharacterModule
#Импорт класса НПС
import NPCModule
#Импорт класса для чтения тхт сценариев
import readfile

pygame.init()

#Экран
Width = 900
Height = 700

#Анимация
motion = 'Stop'
STOP = 'Stop'
animCount = 0
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

#Дисплей
sc = pygame.display.set_mode((Width, Height))

#Заполнение sс
sc.fill((0, 0, 0))

#Анимация основная. В данном случае активируется если персонаж не двигался некоторое время.
mnList = [pygame.image.load('sp_humans/Stay10001.png').convert_alpha(), pygame.image.load('sp_humans/Stay10002.png').convert_alpha(), pygame.image.load('sp_humans/Stay10003.png').convert_alpha(),
        pygame.image.load('sp_humans/Stay10004.png').convert_alpha(), pygame.image.load('sp_humans/Stay10005.png').convert_alpha(),
    pygame.image.load('sp_humans/Stay10006.png').convert_alpha(), pygame.image.load('sp_humans/Stay10007.png').convert_alpha()]

#Основная картинка персонажа. Отображается во время остановки. Я хз как правильно сформулировать...
mnPick = pygame.image.load('sp_humans/Stay10000.png').convert_alpha()
mnPick1 = pygame.image.load('sp_humans/Stay10000.png').convert_alpha()
#Анимация движения влево.
LAnim = [pygame.image.load('sp_humans/Walk0000.png').convert_alpha(), pygame.image.load('sp_humans/Walk0001.png').convert_alpha(),
         pygame.image.load('sp_humans/Walk0002.png').convert_alpha(), pygame.image.load('sp_humans/Walk0003.png').convert_alpha(),
    pygame.image.load('sp_humans/Walk0004.png').convert_alpha(), pygame.image.load('sp_humans/Walk0005.png').convert_alpha(),
    pygame.image.load('sp_humans/Walk0006.png').convert_alpha(), pygame.image.load('sp_humans/Walk0007.png').convert_alpha()]

#Анимация движения вправо
RAnim =[pygame.image.load('sp_humans/WalkL0000.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0001.png').convert_alpha(),
         pygame.image.load('sp_humans/WalkL0002.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0003.png').convert_alpha(),
    pygame.image.load('sp_humans/WalkL0004.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0005.png').convert_alpha(),
    pygame.image.load('sp_humans/WalkL0006.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0007.png').convert_alpha()]

#Объект класса MainCharacter. Игровой персонаж
Persona = CharacterModule.MainCharacter('ID', 'TYPE', mnList, 200, 200, mnPick, 0, 'name', 'hp', 'exp', 'lvl', 'damage', False, LAnim, RAnim)  
#Объект класса NPC. Не игровой персонаж на фоне
NPC = NPCModule.NPC('ID', 'TYPE', mnList, 0, 0, mnPick, 0, 'name', 'hp', 'protection', 'imunitet', 'interaction', False, LAnim, RAnim)
sList = [Persona, NPC]
sprt_surf = []

########################################################
#!!!!!!!!!!!!КОД ПОДЛЕЖАЩИЙ РЕПРЕСИЯМ!!!!!!!!!!!!#
########################################################

#sprt = ('slav_1.jpg','slav_2.jpg','slav_3.jpg','slav_4.jpg','slav_5.jpg','slav_6.jpg')
#sprt = ('slav_2.jpg','slav.png'

#slavia = pygame.sprite.Group()

#Рисунки и их координаты

##for i in range(len(sprt)):
##    sq = Window_Dialog.Pictures('sp_humans/'+sprt[i], 600, 700, slavia)
##    sq.moveLeft()
##    sq.moveLeft()
##    sprt_surf.append(sq)
##

########################################################
#!!!!!!!!!!!!КОНЕЦ РАСТРЕЛЬНОГО СПИСКА!!!!!!!!!!!!#
########################################################

#Задний фон
bacpick = Window_Dialog.Pictures('sp_world/back_standart.jpg', Width, Height)
#print(bacpick.path)

#отрисовка окна с рисунками
window = Window_Dialog.GameWindow(Width, Height, bacpick, sprt_surf,sList)

sc.blit(window.drawGameWind(),(0,0))

########################################################
#!!!!!!!!!!!!КОД ПОДЛЕЖАЩИЙ РЕПРЕСИЯМ!!!!!!!!!!!!#
########################################################

###        
##r = readfile.TextRead('proba').readScene()
##r.reverse()
##print(r)
##
##font_title = pygame.font.SysFont(None, 20)
##
##font_text = pygame.font.SysFont(None, 20)

########################################################
#!!!!!!!!!!!!КОНЕЦ РАСТРЕЛЬНОГО СПИСКА!!!!!!!!!!!!#
########################################################


while 1:
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            exit()
        #Команды на клавиши
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        else:
            motion = STOP
        
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
               pass

        #Инструкции по передвижению
        if motion == LEFT:
            sList[0].setX(sList[0].getX()+10)
            print(sList[0].getX())
            
        elif motion == RIGHT:
            pass
        elif motion == UP:
            pass
        elif motion == DOWN:
            pass
        elif motion == STOP:
            pass
 
    pygame.display.update()
 
    pygame.time.delay(30)

