import pygame 

STOP = 'STOP'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'

class GameWindow:
    def __init__(self, Width, Height, Backp, ObjList = None):
        self.width = Width
        self.height = Height
        self.backpic = pygame.image.load('sp_world/'+Backp).convert_alpha()
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
        
        pygame.display.update()

    def updateWindow(self):
        #self.back.fill((255,255,255))

        self.back.blit(self.backpic, (0,0))

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
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                    
                if i.getMotion() == RIGHT:
                    if i.getAnimCount() <= len(LAnim)-1:
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                if i.getMotion() == UP:
                    if i.getAnimCount() <= len(LAnim)-1:
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(LAnim[i.getAnimCount()], (i.getX(),i.getY()))
                    
                if i.getMotion() == DOWN:
                    if i.getAnimCount() <= len(LAnim)-1:
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))
                        i.setAnimCount(i.getAnimCount()+1)
                    else:
                        i.setAnimCount(0)
                        self.back.blit(RAnim[i.getAnimCount()], (i.getX(),i.getY()))

                if i.getMotion() == STOP:
                    self.back.blit(i.getMainPICK(), (i.getX(), i.getY()))
                
        return self.back
