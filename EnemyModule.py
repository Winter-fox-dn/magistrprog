from NPCModule import NPC

#Класс враждебных Неигровых персонажей
class Enemy(NPC):
    def __init__(self,ID, TYPE, MainList, x, y, MainPick, name, hp, protection, imunitet, interaction, isFrendly, EXP, boss, lvl, damage, LeftANIM, RightANIM):
        NPC.__init__(self, ID, TYPE, name, hp, protection, imunitet, interaction, isFrendly, LeftANIM, RightANIM)
        self.__EXP = EXP
        self.__boss = boss
        self.__LVL = lvl
        self.__damage = damage

#Инкапсуляция 

    def getEXP(self):
        return self.__EXP

    def setEXP(self, exp):
        self.__EXP = exp

    def getBoss(self):
        return self.__boss

    def setBoss(self, boss):
        self.__boss = boss
    
    def getLvl(self):
        return self.__LVL

    def setLvl(self, lvl):
        self.__LVL = lvl
        
    def getDamage(self):
        return self.__damage

    def setDamage(self, damage):
        self.__damage = damage
    
