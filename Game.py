
from character import Char
from Arena_Class import Arena

class Game():
    def __init__(self,character_class_configs):
        self.characterInfo = character_class_configs
        self.characterCounter = 0
        self.characters = dict()
    
    def generateCharacter(self, character_type, char_name):
        C = Char(self.characterInfo, character_type, char_name)
        self.characterCounter += 1
        self.characters[C.name] = C

    
    def initializeArena(self, char1_name, char2_name):
        char1 = self.characters[char1_name]
        char2 = self.characters[char2_name]
        self.A = Arena(char1, char2)
