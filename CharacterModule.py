from GameClassOBJ import GameOBJ

class Character(GameOBJ):
    def __init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount, Motion, name, hp,LeftANIM, RightANIM):
        GameOBJ.__init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount)
        self.X_win = x
        self.Y_win = y
        self.__Name = name
        self.__HP = hp
        self.__LeftANIM = LeftANIM
        self.__RightANIM = RightANIM
        self.__Motion = Motion

    #Инкапсуляция
    def getName(self):
        return self.__Name

    def setName(self, name):
        self.__Name = name
    
    def getHP(self):
        return self.__HP

    def setHP(self, hp):
        self.__HP = hp

    def getLeftANIM(self):
        return self.__LeftANIM

    def setLeftANIM(self, LeftANIM):
        self.__LeftANIM = LeftANIM

    def getRightANIM(self):
        return self.__RightANIM

    def setRightANIM(self, RightANIM):
        self.__RightANIM = RightANIM

    def getMotion(self):
        return self.__Motion
    
    def setMotion(self, motion):
        self.__Motion = motion
    
