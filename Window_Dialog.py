import pygame 

#Удалить к черту мб и не нужен
class Pictures(pygame.sprite.Sprite):
    
    def __init__(self, path, width, height, group = None, x = 0, y = 0):
        #Наследование класса спрайт
        pygame.sprite.Sprite.__init__(self)
        # путь к картинке
        self.path = path
        # загруэаем картинку
        self.surf = pygame.image.load(self.path).convert_alpha()
        #ширина
        self.width = width
        #высота
        self.height = height

        #Установки х и у
        if x == 0 and y == 0:
            self.x = width
            self.y = height
        else:
            self.x = 397 + x
            self.y = height
        #отрисовка
        self.surf_rect = self.surf.get_rect(bottomright =(self.x, self.y))
        if group == None:
            pass
        else:
            self.add(group)

            
    def moveRight(self):
        self.x += self.width*0.1
        self.surf_rect = self.surf.get_rect(bottomright =(self.x, self.y))

        
    def moveLeft(self):
        self.x -= self.width*0.1
        self.surf_rect = self.surf.get_rect(bottomright =(self.x, self.y))

class GameWindow:
    def __init__(self, Width, Height, Backp, PickList = None, ObjList = None):
        self.width = Width
        self.height = Height
        self.backpic = Backp
        self.picklist = PickList
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

        self.back.blit(self.backpic.surf, self.backpic.surf_rect)

        pygame.display.update()

    def drawDialogWind1(self):
 
##        self.back.fill((255,255,255))
##
##        self.back.blit(self.backpic.surf, self.backpic.surf_rect)

        for i in self.picklist:
            self.back.blit(i.surf, i.surf_rect)

        self.back.blit(self.text_dialog, (0, self.height*0.7))

        return self.back
    
    def drawDialogWind2(self):
##        
##        self.back.fill((255,255,255))
##
##        self.back.blit(self.backpic.surf, self.backpic.surf_rect)

        for i in self.picklist:
            self.back.blit(i.surf, i.surf_rect)
        
        
        self.back.blit(self.text_dialog, (0, 0))

        return self.back

    def drawGameWind(self):
        #Прорисовка объектов на экране 
        if self.OBJList == None:
            pass
        else:
            #self.back.blit(self.OBJ
            pass
        return self.back
