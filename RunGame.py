

from Game import Game
from character import Char
from Shop_Class import shop
from itemClass import item
import json


with open("character_class_configs.json") as f:
    reference_class_dict = json.load(f)
    
with open('item_config.json') as data_file:
    item_data = json.load(data_file)


G = Game(reference_class_dict, item_data)
G.generateCharacter('knight','Phil')
G.generateCharacter('mage','Draco')

G.initializeShop()
print(G.shop.coin)

G.shop.fill_up_shop()
print(G.shop.armory)

item_to_buy = list(G.shop.armory.keys())[0]
print(f'Eli is buying a {item_to_buy}')

G.shop.purchase_item(item_to_buy)
print(G.shop.armory)

# G.initializeArena('Phil','Draco')
# print(G.characters.keys())
# G.A.combat()