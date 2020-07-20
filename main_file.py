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
motion = 'STOP'
STOP = 'STOP'
animCount = 0
LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'


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
RAnim = [pygame.image.load('sp_humans/Walk0000.png').convert_alpha(), pygame.image.load('sp_humans/Walk0001.png').convert_alpha(),
         pygame.image.load('sp_humans/Walk0002.png').convert_alpha(), pygame.image.load('sp_humans/Walk0003.png').convert_alpha(),
    pygame.image.load('sp_humans/Walk0004.png').convert_alpha(), pygame.image.load('sp_humans/Walk0005.png').convert_alpha(),
    pygame.image.load('sp_humans/Walk0006.png').convert_alpha(), pygame.image.load('sp_humans/Walk0007.png').convert_alpha()]
#Анимация движения вправо
LAnim =[pygame.image.load('sp_humans/WalkL0000.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0001.png').convert_alpha(),
         pygame.image.load('sp_humans/WalkL0002.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0003.png').convert_alpha(),
    pygame.image.load('sp_humans/WalkL0004.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0005.png').convert_alpha(),
    pygame.image.load('sp_humans/WalkL0006.png').convert_alpha(), pygame.image.load('sp_humans/WalkL0007.png').convert_alpha()]

background = pygame.image.load('sp_world/back_standart.jpg').convert_alpha()

#Объект класса MainCharacter. Игровой персонаж
Persona = CharacterModule.MainCharacter('ID', 'TYPE', mnList, 200, 200, mnPick, 0, STOP, 'name', 'hp', 'exp', 'lvl', 'damage', False, LAnim, RAnim)  

#Объект класса NPC. Не игровой персонаж на фоне
NPC = NPCModule.NPC('ID', 'TYPE', mnList, 0, 0, mnPick, 0, STOP,'name', 'hp', 'protection', 'imunitet', 'interaction', False, LAnim, RAnim)
sList = [Persona, NPC]

#отрисовка окна с рисунками
window = Window_Dialog.GameWindow(Width, Height, 'back_standart.jpg', sList)

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
                sList[0].setMotion(LEFT)
                
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
                sList[0].setMotion(RIGHT)
                
            elif i.key == pygame.K_UP:
                motion = UP
                sList[0].setMotion(UP)
                
            elif i.key == pygame.K_DOWN:
                motion = DOWN
                sList[0].setMotion(DOWN)
                
        else:
            motion = STOP
            sList[0].setMotion(STOP)
        
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
               pass

    #Инструкции по передвижению
    if motion == LEFT:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setX(sList[0].getX()-10)
        
    elif motion == RIGHT:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setX(sList[0].getX()+10)
        
    elif motion == UP:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setY(sList[0].getY()-10)
        
    elif motion == DOWN:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setY(sList[0].getY()+10)
        
    elif motion == STOP:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
 
    pygame.display.update()
 
    pygame.time.delay(30)

