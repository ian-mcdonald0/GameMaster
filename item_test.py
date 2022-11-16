from flask_app.models.item import *
import json


with open('item_config.json') as data_file:
    data = json.load(data_file)


d1 = Item(data["rusty spoon"])
d2 = Item(data["prison shank"])
print(d1.damage)
print(d1.imbue)
print(d2.imbue)


d3 = Item(data["Ian's bludgeon"])
d4 = Item(data["Josh's long bow"])
d5 = Item(data["kite shield"])
print(d3.imbue)
print(d4.damage)
print(d5.defense)