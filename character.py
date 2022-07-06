import random
import json


class char():
    def __init__(self, class_reference, character_type, char_name):

        # self.reference_class_dict = self.access_class_reference()
        self.reference_class_dict = class_reference
        self.name = char_name
        self.type = character_type
        self.initialize_stats()

        self.equipment = {'armor' : None, 'weapon': None}
        

    # def access_class_reference(self):
    #     with open("character_class_configs.json") as f:
    #         reference_class_dict = json.load(f)

        # return reference_class_dict

    def initialize_stats(self):

        stats = self.reference_class_dict[self.type]

        self.max_health = stats["base_health"] + random.randrange(1,7)
        self.current_health = self.max_health
        self.physical_attack = stats["base_physical_attack"]
        self.magic_attack = stats["base_magic_attack"]
        self.armor = stats["base_armor"]



    def equip_item(self, item, swap_out = False):
        assert item.equipment == True, 'item is not equipment so it may not be equipped'

        equip_type = item.equipment_type
        if swap_out:
            self.equipment[equip_type] = item
        elif self.equipment[equip_type] == None:
            self.equipment[equip_type] = item
        elif (self.equipment[equip_type] != None) & (swap_out == False):
            print('equipment already equipped in this slot')