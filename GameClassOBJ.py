class GameOBJ:
    def __init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount):
        self.__ID = ID
        self.__TYPE = TYPE
        self.__MainLIST = MainList
        self.__X = x
        self.__Y = y        
        self.__MainPICK = MainPick
        self.__AnimCount = AnimCount

    def getID(self):
        return self.__ID

    def setID(self, ID):
        self.__ID = ID

    def setTYPE(self,TYPE):
        self.__TYPE = TYPE

    def getTYPE(self):
        return self.__TYPE

    def getX(self):
        return self.__X

    def setX(self, X):
        self.__X = X

    def getY(self):
        return self.__Y

    def setY(self, Y):
        self.__Y = Y

    def getAnimLIST(self):
        return self.__MainLIST

    def setAnimLIST(self, MainLIST):
        self.__MainLIST = MainLIST

    def getMainPICK(self):
        return self.__MainPICK

    def setMainPICK(self, MainPICK):
        self.__MainPICK = MainPICK

    def getAnimCount(self):
        return self.__AnimCount

    def setAnimCount(self, num):
        self.__AnimCount = num
