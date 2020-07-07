from GameClassOBJ import GameOBJ 

#Класс Не игровых персонажей
class NPC(GameOBJ):
    def __init__(self, ID, TYPE, name, hp, protection, imunitet, interaction, isFrendly, LeftANIM, RightANIM):
       GameOBJ.__init__(self, ID, TYPE)
       self.__Name = name
       self.__HP = hp
       self.__Protect = protection
       self.__Imunitet = imunitet
       self.__Interaction = interaction
       self.__IsFrendly = isFrendly
       self.__LeftANIM = LeftANIM
       self.__RightANIM = RightANIM

    #Инкапсуляция
    def getName(self):
        return self.__Name

    def setName(self, name):
        self.__Name = name
    
    def getHP(self):
        return self.__HP

    def setHP(self, hp):
        self.__HP = hp
    
    def getProtect(self):
        return self.__Protect

    def setProtect(self, pro):
        self.__Protect = pro

    def getImunitet(self):
        return self.__Imunitet

    def setImunitet(self, im):
        self.__Imunitet = im
        
    def getInteraction(self):
        return self.__Interaction

    def setInteraction(self, inter):
        self.__Interaction = inter
        
    def getIsFrendly(self):
        return self.__IsFrendly

    def setIsFrendly(self, frn):
        self.__IsFrendly = frn

    def getLeftANIM(self):
        return self.__LeftANIM

    def setLeftANIM(self, LeftANIM):
        self.__LeftANIM = LeftANIM

    def getRightANIM(self):
        return self.__RightANIM

    def setRightANIM(self, RightANIM):
        self.__RightANIM = RightANIM
