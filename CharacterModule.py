from GameClassOBJ import GameOBJ

#Главный персонаж
class MainCharacter(GameOBJ):
    def __init__(self, ID, TYPE, name, hp, exp, lvl, damage, isEffect, LeftANIM, RightANIM):
        GameOBJ.__init__(self, ID, TYPE)
        self.__name = name
        self.__HP = hp
        slef.__LVL = lvl
        self.__damage = damage
        self.__isEffect = isEffect
        self.__LeftANIM = LeftANIM
        self.__RightANIM = RightANIM
        
#Инкапсуляция
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getHP(self):
        return self.__HP

    def setHP(self, hp):
        self.__HP = hp

    def getLVL(self):
        return self.__LVL

    def setName(self, lvl):
        self.__LVL = lvl

    def getDamage(self):
        return self.__damage

    def setDamage(self, dam):
        self.__damage = dam

    def getIsEffect(self):
        return self.__isEffect

    def setIsEffect(self, isef):
        self.__isEffect = isef

    def getLeftANIM(self):
        return self.__LeftANIM

    def setLeftANIM(self, LeftANIM):
        self.__LeftANIM = LeftANIM

    def getRightANIM(self):
        return self.__RightANIM

    def setRightANIM(self, RightANIM):
        self.__RightANIM = RightANIM
