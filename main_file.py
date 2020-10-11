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


backgr = Window_Dialog.GameSurface(1000, 1000, 'backfon.jpg')

#Объект класса MainCharacter. Игровой персонаж
Persona = GameCharacterModule.MainCharacter('ID', 'TYPE', mnList, 400, 300, mnPick, 0, STOP, 'name', 'hp', 'exp', 'lvl', 'damage', False, LAnim, RAnim)  

print("Персонаж -> X:",Persona.getX()," Y: ", Persona.getY()) 
#Объект класса NPC. Не игровой персонаж на фоне
NPC = NPCModule.NPC('ID', 'NPC', mnList, backgr.getX()-100, backgr.getY(), mnPick, 0, STOP,'name', 'hp', 'protection', 'imunitet', 'interaction', False, LAnim, RAnim)
sList = [Persona, NPC]

#отрисовка окна с рисунками
window = Window_Dialog.GameWindow(Width, Height, backgr, sList)

sc.blit(window.drawGameWind(),(0,0))

#Тест передвижения
def moveNPC():
    #выбор направления
    if sList[1].getX() <= window.Back.getX()-100:
        sList[1].setMotion(RIGHT)
        
    if sList[1].getX() >= window.Back.getX()+window.Back.getWidth()-150:
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
##                if sList[0].getXwin() <= window.getX1()-150:
##                    motion = STOP
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
                sList[0].setMotion(RIGHT)
##                if sList[0].getXwin() >= window.getX2()-150:
##                    motion = STOP
                
            elif i.key == pygame.K_UP:
                motion = UP
                sList[0].setMotion(UP)
##                if sList[0].getYwin() <= window.getY1()-150:
##                    motion = STOP
                
            elif i.key == pygame.K_DOWN:
                motion = DOWN
                sList[0].setMotion(DOWN)
##                if sList[0].getYwin() >= window.getY2()-150:
##                    motion = STOP
                
        else:
            motion = STOP
            sList[0].setMotion(STOP)
        
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
               pass
        
    #Инструкции по передвижению
    moveNPC()
    if motion == LEFT and Persona.getXwin() != window.getX1()-100:
        #Обновление окна и передвижение персонажей
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))

        sList[0].setX(sList[0].getX()-10)
        sList[0].setXwin(sList[0].getXwin()-10)
         
    elif motion == LEFT and Persona.getXwin() <= window.getX1()-100:
        #Передвижение заднего фона в заданных рамках
        #Ограничение по полю
        #Я чет выводил "формулу" определения конца окна, хотя можно просто 0 написать... Мда... Не важно......
        #НЕ ВАЖНО window.Back.getWidth()*(-1)+window.getX1()+Width
        #Определение правой крайней рамки идет через схему (Ширина карты + первая граница передвижения + ширина окна) 
        if window.Back.getX() >= 0:
            pass
##            print(window.Back.getX(),'||',window.Back.getWidth()*(-1)+window.getX1()+Width)
        else:
            window.Back.setX(window.Back.getX()+10)
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))

    elif motion == RIGHT and Persona.getXwin() != window.getX2()-150:
        #Обновление окна и передвижение персонажей
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        
        sList[0].setX(sList[0].getX()+10)
        sList[0].setXwin(sList[0].getXwin()+10)
        
    elif motion == RIGHT and Persona.getXwin() >= window.getX2()-150:
        #Передвижение заднего фона в заданных рамках
        #Определение правой крайней рамки идет через схему (Ширина карты + вторая граница передвижения + (ширина окна - вторая граница передвижения))         
        if window.Back.getX() <= window.Back.getWidth()*(-1)+window.getX2()+(Width - window.getX2()):
            print('==>',window.Back.getX(),'||',window.Back.getWidth()*(-1)+window.getX2()+(Width - window.getX2()))
##            print(window.Back.getWidth()*(-1)+window.getX2()+(Width - window.getX2()))
##            sList[0].setX(sList[0].getX()+10)
##            sList[0].setXwin(sList[0].getXwin()+10)
        else:
            window.Back.setX(window.Back.getX()-10)
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))

    elif motion == UP and Persona.getYwin() != window.getY1()-150:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        
        sList[0].setY(sList[0].getY()-10)
        sList[0].setYwin(sList[0].getYwin() - 10)
        
    elif motion == UP and Persona.getYwin() >= window.getY1()-150:
        #Передвижение заднего фона в заданных рамках
        if window.Back.getY() >= 0 :
            print(window.Back.getY(),'||',window.Back.getHeight())
        else:
            window.Back.setY(window.Back.getY()+10)            
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
        
    elif motion == DOWN and Persona.getYwin() != window.getY2()-250:
        #Обновление окна и передвижение персонажей
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))

        sList[0].setY(sList[0].getY()+10)
        sList[0].setYwin(sList[0].getYwin()+10)
##        print(window.Back.getY(),"\_(T_T)_|",(window.Back.getHeight()-window.getY2())*(-1))
                
    elif motion == DOWN and Persona.getYwin() <= window.getY2()-250:
        #Передвижение заднего фона в заданных рамках
        
        if window.Back.getY() <=(window.Back.getHeight()-window.getY2())*(-1)+(Height - window.getY2()):
            print(window.Back.getY(),'||',(window.Back.getHeight()-window.getY2())*(-1)+(Height - window.getY2()))
        else:
            window.Back.setY(window.Back.getY()-10)
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
    
    elif motion == STOP:
        sc.blit(window.updateWindow(),(0,0))
        sc.blit(window.drawGameWind(),(0,0))
 
    pygame.display.update()
    
    pygame.time.delay(30)

