from CharacterModule import Character 

#Класс Неигровых персонажей
class NPC(Character):
    def __init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount, Motion, name, hp, protection, imunitet, interaction, isFrendly, LeftANIM, RightANIM):
       Character.__init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount, Motion, name, hp, LeftANIM, RightANIM)
       self.__Protect = protection
       self.__Imunitet = imunitet
       self.__Interaction = interaction
       self.__IsFrendly = isFrendly
       
    #Инкапсуляция    
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
