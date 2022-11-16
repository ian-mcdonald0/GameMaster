import random
import json
import flask_app.models.spells as Spells
from flask_app.models.spells import Spells
from flask_app.models.item import Item

class Shop():
    def __init__(self, game, item_ref_dict):
        self.coin = 100
        self.armory = dict()
        # self.armor = dict()
        # self.weapons = dict()
        # self.consumables = dict()
        self.items_on_layaway = item_ref_dict
        self.game = game
        # self.fill_up_shop()


    def fill_up_shop(self, item_num = 2):

        if item_num == 1:
            item_max = len(self.items_on_layaway.keys())
            item_key = random.randint(0,item_max -1)
            item_name = list(self.items_on_layaway.keys())[item_key]

            new_item = self.game.generate_item(item_name)

            self.armory[new_item.name] = new_item
        else:
            for i in range(item_num):
                item_max = len(self.items_on_layaway.keys())
                item_key = random.randint(0,item_max -1)
                item_name = list(self.items_on_layaway.keys())[item_key]

                new_item = self.game.generate_item(item_name)

                self.armory[new_item.name] = new_item
        # instantiate the item

    def show_me_your_wares(self):
        print(self.armory.keys())

    def purchase_item(self, item_name):
        if item_name not in list(self.armory.keys()):
            print('We have no such shit!!')
            return
        else:
            item_bought = self.armory[item_name]
            del self.armory[item_name]

            self.fill_up_shop(item_num = 1)

            return item_bought

