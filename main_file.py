#Импорт класса отрисовывающего окна
from Window_Dialog import pygame
import Window_Dialog
#Импорт класса ГГ
import GameCharacterModule
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


backgr = Window_Dialog.GameSurface(1000, 700, 'backfon.jpg')

#Объект класса MainCharacter. Игровой персонаж
Persona = GameCharacterModule.MainCharacter('ID', 'TYPE', mnList, 100, 100, mnPick, 0, STOP, 'name', 'hp', 'exp', 'lvl', 'damage', False, LAnim, RAnim)  

print("Персонаж -> X:",Persona.getX()," Y: ", Persona.getY()) 
#Объект класса NPC. Не игровой персонаж на фоне
NPC = NPCModule.NPC('ID', 'NPC', mnList, backgr.x-100, backgr.y, mnPick, 0, STOP,'name', 'hp', 'protection', 'imunitet', 'interaction', False, LAnim, RAnim)
sList = [Persona, NPC]

#отрисовка окна с рисунками
window = Window_Dialog.GameWindow(Width, Height, backgr, sList)

#ДОБАВИТЬ И ОБНОВИТЬ ГЕТЕРЫ И СЕТЕРЫ

###################################################
sc.blit(window.drawGameWind(),(0,0))
###################################################

#Тест передвижения
def moveNPC():
    #выбор направления
    if sList[1].getX() <= window.Back.x-100:
        sList[1].setMotion(RIGHT)
    if sList[1].getX() >= window.Back.x+window.Back.width-150:
        print(window.Back.width-150)
        sList[1].setMotion(LEFT)
    #Передвижение нпс
    if sList[1].getMotion() == RIGHT:
        sList[1].setX(sList[1].getX()+10)
    if sList[1].getMotion() == LEFT:
        sList[1].setX(sList[1].getX()-10)
        
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
                if sList[0].X_win <= window.x1-150:
                    motion = STOP
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
                sList[0].setMotion(RIGHT)
                if sList[0].X_win >= window.x2-150:
                    motion = STOP
                
            elif i.key == pygame.K_UP:
                motion = UP
                sList[0].setMotion(UP)
                if sList[0].Y_win <= window.y1-150:
                    motion = STOP
                
            elif i.key == pygame.K_DOWN:
                motion = DOWN
                sList[0].setMotion(DOWN)
                if sList[0].Y_win >= window.y2-150:
                    motion = STOP
                
        else:
            motion = STOP
            sList[0].setMotion(STOP)
        
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
               pass
        
    #Инструкции по передвижению
    moveNPC()
    ##ДОБАВИТЬ ГЕТЕРОВ И СЕТЕРОВ
    if motion == LEFT and Persona.X_win != window.x1-150:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setX(sList[0].getX()-10)
        #################################
        sList[0].X_win -= 10
        #################################
        #print('X',sList[0].X_win)
    elif motion == LEFT and Persona.X_win <= window.x1-150:
        window.Back.x+=10
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))

        #################################
    elif motion == RIGHT and Persona.X_win != window.x2-150:
        #################################
        print(RIGHT)
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        #################################
        sList[0].setX(sList[0].getX()+10)
        #################################
        sList[0].X_win += 10
        #print('X',sList[0].X_win)
    elif motion == RIGHT and Persona.X_win >= window.x2-150:
        window.Back.x-=10
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))

        #################################
    elif motion == UP and Persona.Y_win != window.y1-150:
        #################################
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setY(sList[0].getY()-10)
        #################################
        sList[0].Y_win -= 10
        #################################
        #print('Y:',sList[0].Y_win)
        
    elif motion == UP and Persona.Y_win >= window.y1-150:
        window.Back.y+=10
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        
    #################################
    elif motion == DOWN and Persona.Y_win != window.y2-250:
        #################################
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        sList[0].setY(sList[0].getY()+10)
        #################################
        sList[0].Y_win += 10
        #################################
        
    elif motion == DOWN and Persona.Y_win <= window.y2-250:
        window.Back.y-=10
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
    
    elif motion == STOP:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
 
    pygame.display.update()
    
    pygame.time.delay(30)

