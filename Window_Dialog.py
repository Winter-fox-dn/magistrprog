import pygame 
from array import *
import numpy as np

STOP = 'STOP'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'


class GameSurface:
    def __init__(self,Width, Height, Backp):
        self.width = Width
        self.height = Height
        self.backpic = pygame.image.load('sp_world/'+Backp).convert_alpha() 
        k2 = int()#
        k3 = int()#
        
        #Определениие размерров массива и его создание.
        #Если ячейка меньше или равна четверти то она не учитыается.
        #Прорисовка сетки 
        for i in range(0, self.width, 30):
            pygame.draw.line(self.backpic, (255,255,255),[i,0],[i, self.height])
            if (self.width - i) <= 7.5:
                print(self.width - i)
            else:
                k2 +=1
            k +=1
        for i in range(0,self.height, 30):
            pygame.draw.line(self.backpic, (255,255,255),[0,i],[self.width, i])
            if (self.height - i) <= 7.5:
                print(self.height - i)
            else:
                k3 +=1
            k1 +=1
            
        #Создание квадратика 30Х30
        surf1 = pygame.Surface((30, 30))
        surf1.fill((220, 200, 0))  # желтая

        rect = pygame.Rect((30, 30, 0, 0))
        self.backpic.blit(surf1, rect)

        #массив 
        a = np.zeros((k3,k2))

        print(a)
        #Отладка
        print("Столбцы: ",k2 ," Строки: ",k3)


    def showGrid():
        k = int()#временно для откладки 
        k1 = int()##временно для откладки
        for i in range(0, self.width, 30):
            pygame.draw.line(self.backpic, (255,255,255),[i,0],[i, self.height])
            k +=1
        for i in range(0,self.height, 30):
            pygame.draw.line(self.backpic, (255,255,255),[0,i],[self.width, i])
            k1 +=1
        print("Вертикальных линий: ",k ," Горизонтальных линий: ",k1)


class GameWindow:
    def __init__(self, Width, Height, Backp, ObjList = None):
        self.width = Width
        self.height = Height
        self.backpic = pygame.image.load('sp_world/'+Backp).convert_alpha()
        #self.backpic = pygame.transform.scale(self.backpic, (10000,10000))
        
        self.OBJList = ObjList        
        #Установка заднего фона
        self.back = pygame.Surface((self.width, self.height))
        #Установка диалогового окна
        self.text_dialog = pygame.Surface((self.width,self.height))
        #Заполнение диалогового окна
        self.text_dialog.fill((160,0,100))
        #Установка прозрачности
        self.text_dialog.set_alpha(160)
        
        self.back.fill((255,255,255))

        self.back.blit(self.backpic, (0,0))
        #Сетка
        #pygame.draw.line(self.back, (255,255,255),[0,100],[200, 200])    
        
        pygame.display.update()

    def updateWindow(self):
        #self.back.fill((255,255,255))

        self.back.blit(self.backpic, (0,0))
        
        #self.drawGrid()
        #pygame.display.update()

        return self.back

    def drawDialogWind1(self):

        for i in self.picklist:
            self.back.blit(i.surf, i.surf_rect)

        self.back.blit(self.text_dialog, (0, self.height*0.7))

        return self.back
    
    def drawDialogWind2(self):

        for i in self.picklist:
            self.back.blit(i.surf, i.surf_rect)
        self.back.blit(self.text_dialog, (0, 0))

        return self.back

    def drawGameWind(self):
        #Сетка
        #self.drawGrid()
        surf = pygame.Surface((70,140))
        surf.fill((255,0,0))
        #Прорисовка объектов на экране 
        if self.OBJList == None:
            pass
        else:
            for i in self.OBJList:
                LAnim = i.getLeftANIM()
                RAnim = i.getRightANIM()
                MNList = i.getAnimLIST()
                
                if i.getMotion() == LEFT:
                    if i.getAnimCount() <= len(LAnim)-1:
                        
                        self.back.blit(surf, (i.getX()+90,i.getY()+120))                                  
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                    
                if i.getMotion() == RIGHT:
                    if i.getAnimCount() <= len(LAnim)-1:
                        self.back.blit(surf, (i.getX()+90,i.getY()+120))
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                if i.getMotion() == UP:
                    if i.getAnimCount() <= len(LAnim)-1:
                        self.back.blit(surf, (i.getX()+90,i.getY()+120))
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                if i.getMotion() == DOWN:
                    if i.getAnimCount() <= len(LAnim)-1:
                        self.back.blit(surf, (i.getX()+90,i.getY()+120))
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))

                if i.getMotion() == STOP:
                    self.back.blit(surf, (i.getX()+90,i.getY()+120))
                    self.back.blit(i.getMainPICK(), (i.getX(), i.getY()))
                
        return self.back
