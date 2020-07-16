from NPCModule import NPC

class Frendly(NPC):
    def __init__(self,ID, TYPE, MainList, x, y, MainPick,name, hp, protection, imunitet, interaction, isFrendly, Dialog = 0, Scene = 0, LeftANIM, RightANIM):
        NPC.__init__(self, ID, TYPE, MainList, x, y, MainPick, name, hp, protection, imunitet, interaction, isFrendly, LeftANIM, RightANIM)
        self.__ListDialog = Dialog
        self.__ListScene = Scene

    def getListDialog(self):
        return self.__ListDialog

    def setListDialog(self, dil):
        self.__ListDialog = dil

    def getListScene(self):
        return self.__ListScene

    def setListScene(self, scen):
        self.__ListScene = scen

    
