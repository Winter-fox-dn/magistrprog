from GameClassOBJ import GameOBJ

#Физические объекты
class PhisOBJ(GameOBJ):
    def __init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount, typeOBJ, destruction, hp, isPickUp, SecondEffect):
        GameOBJ.__init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount)
        self.__typeOBJ = typeOBJ
        self.__destr = destruction
        self.__HP = hp
        self.__isPickUp = isPickUp
        self.__SecondEffect = SecondEffect
       
#Инкапсуляция
    def getTypeOBJ(self):
        return self.__typeOBJ

    def setTypeOBJ(self, typobj):
        self.__typeOBJ = typobj
        
    def getDestr(self):
        return self.__destr

    def setDestr(self, destr):
        self.__destr = destr

    def getHP(self):
        return self.__HP

    def setHP(self, hp):
        self.__HP = hp

    def getIsPickUp(self):
        return self.__isPickUp

    def setIsPickUp(self, isPick):
        self.__isPickUp = isPick

    def getSecondEffect(self):
        return self.__SecondEffect

    def setSecondEffect(self, SecondEffect):
        self.__SecondEffect = SecondEffect
