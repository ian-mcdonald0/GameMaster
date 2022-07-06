from itemClass import *
import json


with open('item_config.json') as data_file:
    data = json.load(data_file)


d1 = item(data["rusty spoon"])
d2 = item(data["prison shank"])
print(d1.damage)
print(d1.imbue)
print(d2.imbue)


d3 = item(data["Ian's bludgeon"])
d4 = item(data["Josh's long bow"])
d5 = item(data["kite shield"])
print(d3.imbue)
print(d4.damage)
print(d5.defense)