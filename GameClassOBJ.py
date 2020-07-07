class GameOBJ:
    def __init__(self, ID, TYPE, MainList = 0, x = 0, y = 0, MainPick = 0):
        self.__ID = ID
        self.__TYPE = TYPE
        self.__X = x
        self.__Y = y
        self.__MainLIST = MainList
        self.__MainPICK = MainPick

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
        return self.MainPICK

    def setMainPICK(self, MainPICK):
        self.MainPICK = MainPICK
