from GameClassOBJ import GameOBJ

#Класс *бог простит* трапов
class Trap(GameOBJ):
    def __init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount, trapType, DPS, Effects):
        GameOBJ.__init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount)
        self.__trapType = trapType
        self.__DPS = DPS
        self.__effects = Effects

    #Инкапсуляция
    def getTrapType(self):
        return self.__trapType

    def setTrapType(self, tt):
        self.__trapType = tt

    def getDPS(self):
        return self.__DPS

    def setDPS(self, dps):
        self.__DPS = dps
        
    def getEffects(self):
        return self.__effects

    def setEffects(self, ef):
        self.__effects = ef
