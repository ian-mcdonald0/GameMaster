

from flask_app.models.Game import Game
from flask_app.models.character import Char
from Shop_Class import shop
from itemClass import item
import json
from flask_app.models.NonPlayable.Monster import Monster


with open("character_class_configs.json") as f:
    reference_class_dict = json.load(f)
    
with open('item_config.json') as data_file:
    item_data = json.load(data_file)

with open('Monster_class_configs.json') as monster_file:
    monster_class_dict = json.load(monster_file)

G = Game(reference_class_dict, item_data, monster_class_dict)

G.generate_monster('witch')
print(G.monsters)
print(G.monsters['witch'].intellect)

# G.generateCharacter('knight','Phil')
# G.generateCharacter('mage','Draco')

# G.initializeShop()
# print(G.shop.coin)

# G.shop.fill_up_shop()
# print(G.shop.armory)

# C1 = G.characters['Draco']
# C2 = G.characters['Phil']

# C1.buy_item()
# C2.buy_item()

# print(C1.equipment,C2.equipment)

# #item_to_buy = list(G.shop.armory.keys())[0]
# #print(f'Eli is buying a {item_to_buy}')

# #G.shop.purchase_item(item_to_buy)
# #print(G.shop.armory)

# G.initializeArena('Phil','Draco')
# print(G.characters.keys())
# G.A.combat()
