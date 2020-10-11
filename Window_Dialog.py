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
        self.__width = Width
        self.__height = Height
        self.backpic = pygame.image.load('sp_world/'+Backp).convert_alpha()
        self.backpic = pygame.transform.scale(self.backpic, (self.__width, self.__height))
        self.__X = 0
        self.__Y = 0
        k2 = int()#
        k3 = int()#
        #Определениие размерров массива и его создание.
        #Если ячейка меньше или равна четверти то она не учитыается.
        #Прорисовка сетки 
        for i in range(0, self.__width, 30):
            pygame.draw.line(self.backpic, (255,0,0),[i,0],[i, self.__height])
            if (self.__width - i) <= 7.5:
                print(self.__width - i)
            else:
                k2 +=1
            #k +=1
        for i in range(0,self.__height, 30):
            pygame.draw.line(self.backpic, (255,0,0),[0,i],[self.__width, i])
            if (self.__height - i) <= 7.5:
                print(self.__height - i)
            else:
                k3 +=1
            #k1 +=1
            
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
        for i in range(0, self.__width, 30):
            pygame.draw.line(self.backpic, (255,255,255),[i,0],[i, self.__height])
            k +=1
        for i in range(0,self.__height, 30):
            pygame.draw.line(self.backpic, (255,255,255),[0,i],[self.__width, i])
            k1 +=1
        print("Вертикальных линий: ",k ," Горизонтальных линий: ",k1)

    #Инкапсуляция
    def setX(self, x):
        self.__X = x

    def getX(self):
        return self.__X
    
    def setY(self, y):
        self.__Y = y

    def getY(self):
        return self.__Y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
       
class GameWindow:
    def __init__(self,Width, Height, Back, ObjList = None):
        self.__width = Width
        self.__height = Height
        #self.backpic = pygame.transform.scale(self.backpic, (10000,10000))
        self.Back = Back
        self.OBJList = ObjList

        #в конце карты?
        self.isEnd = False

        #Границы передвижения, для ограничения передвижения по экрану 
        self.__x1 = 100
        self.__x2 = 600
        self.__y1 = 100
        self.__y2 = 600

        #Установка заднего фона
        self.back = pygame.Surface((self.__width, self.__height))
        #Установка диалогового окна
        self.text_dialog = pygame.Surface((self.__width,self.__height))
        #Заполнение диалогового окна
        self.text_dialog.fill((160,0,100))
        #Установка прозрачности
        self.text_dialog.set_alpha(160)
        
        self.back.fill((255,255,255))

        self.back.blit(self.Back.backpic, (self.Back.getX(),self.Back.getY()))        
        
        pygame.display.update()

    #Инкапсуляция
    def setX1(self, x):
        self.__x1 = x

    def getX1(self):
        return self.__x1

    def setX2(self, x):
        self.__x2 = x

    def getX2(self):
        return self.__x2
    
    def setY1(self, y):
        self.__y1 = y

    def getY1(self):
        return self.__y1
    
    def setY2(self, y):
        self.__y2 = y

    def getY2(self):
        return self.__y2
    
    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def updateWindow(self):
        self.back.fill((255,255,255))

        self.back.blit(self.Back.backpic, (self.Back.getX(),self.Back.getY()))
        #Прорисовка границ передвижения персонажа 
        pygame.draw.line(self.back, (0,0,255),[self.__x1,0],[self.__x1, self.__height])
        pygame.draw.line(self.back, (0,0,255),[self.__x2,0],[self.__x2, self.__height])
        pygame.draw.line(self.back, (255,0,0),[0,self.__y1],[self.__width, self.__y1])
        pygame.draw.line(self.back, (255,0,0),[0,self.__y2],[self.__width, self.__y2])
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
                        
                        #self.back.blit(surf, (i.getX()+90,i.getY()+120))                                  
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                    
                if i.getMotion() == RIGHT:
                    if i.getAnimCount() <= len(LAnim)-1:
                        #self.back.blit(surf, (i.getX()+90,i.getY()+120))
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                if i.getMotion() == UP:
                    if i.getAnimCount() <= len(LAnim)-1:
                        #self.back.blit(surf, (i.getX()+90,i.getY()+120))
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                if i.getMotion() == DOWN:
                    if i.getAnimCount() <= len(LAnim)-1:
                        #self.back.blit(surf, (i.getX()+90,i.getY()+120))
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))

                if i.getMotion() == STOP:
                    #self.back.blit(surf, (i.getX()+90,i.getY()+120))
                    self.back.blit(i.getMainPICK(), (i.getX(), i.getY()))
                
        return self.back
