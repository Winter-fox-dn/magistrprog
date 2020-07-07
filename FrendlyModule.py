from NPCModule import NPC

class Frendly(NPC):
    def __init__(self,ID, TYPE, name, hp, protection, imunitet, interaction, isFrendly, Dialog, Scene):
        NPC.__init__(self, ID, TYPE, name, hp, protection, imunitet, interaction, isFrendly)
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

    
