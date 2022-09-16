

from Game import Game
from character import Char
import json


with open("character_class_configs.json") as f:
    reference_class_dict = json.load(f)
    
with open('item_config.json') as data_file:
    item_data = json.load(data_file)


G = Game(reference_class_dict)
G.generateCharacter('knight','Phil')
G.generateCharacter('mage','Draco')
G.initializeArena('Phil','Draco')
print(G.characters.keys())
G.A.combat()