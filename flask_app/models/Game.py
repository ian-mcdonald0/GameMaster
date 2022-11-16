
from flask_app.models.character import Char
from flask_app.models.arena import Arena
from flask_app.models.shop import Shop
from flask_app.models.item import Item
from flask_app.models.NonPlayable.Monster import Monster
from flask_app.models.dumbyCharacter import _Dumby

class Game():
    def __init__(self, character_class_configs):
        self.characterInfo = character_class_configs
        # self.itemInfo = item_ref_dict
        self.characterCounter = 0
        self.characters = dict()
        self.monsters = dict()
        # self.MonsterInfo = Monster_class_configs
    
    def generateCharacter(self, character_type, char_name):
        C = Char(self.characterInfo, character_type, char_name, self)
        # C = _Dumby()
        # print(C.names)
        self.characterCounter += 1
        self.characters[C.name] = C

    
    def initializeArena(self, char1_name, char2_name):
        char1 = self.characters[char1_name]
        char2 = self.characters[char2_name]
        self.A = Arena(char1, char2)

    def initializeShop(self):
        itemInfo = self.itemInfo
        self.shop = Shop(self, itemInfo)

    def generate_item(self, item_name):
        item_stats = self.itemInfo[item_name]
        I = Item(item_name, item_stats)
        return(I)

    def generate_monster(self, monster_type):
        M = Monster(self.MonsterInfo, monster_type, self)
        self.monsters[monster_type] = M