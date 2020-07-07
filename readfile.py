
#Получение диалогов персонажа 

class TextRead:
    #Инициализация
    def __init__(self, name_scen):
        self.name_scene = name_scen

        self.file = open('scene_text/'+ self.name_scene + '.txt')#Открываем файл

        #Списки с именами персонажей и их репликами
        self.Char_Dial = list()
        #Списки персонажей
        self.Character_List = list()
        
        
    def getCharacters(self):
        return self.Character_List        

    def readScene(self):
        #Чтение реплик персонажа
        ft = False

        Name_Dialog = list()

        for line in self.file :
            #считывание персонажей с файла
            if "ПЕРСОНАЖИ: " in line:

                line = line.replace('ПЕРСОНАЖИ: ', '')

                line = line.replace('\n', '')

                line = line.replace('.', '')

                self.Character_List = line.split(",")

            if ft == True:

                Name_Dialog.append(line.replace('\n', ''))

                self.Char_Dial.append(Name_Dialog)

                Name_Dialog = list()

                ft = False
                
            for name1 in self.Character_List:
                
                if name1+":" in line:

                    ft = True

                    Name_Dialog.append(name1)
                    
            
        return self.Char_Dial

        
            

    

    

    
