import random

class Monster():
    def __init__(self, class_reference, monster_type, game):

        # self.reference_class_dict = self.access_class_reference()
        self.reference_class_dict = class_reference
        self.type = monster_type
        self.initialize_stats()
        self.alive = True
        self.game = game

        self.equipment = {'armor' : None, 'weapon': None, 'consumable':None}

    def initialize_stats(self):

        stats = self.reference_class_dict[self.type]

        self.max_health = stats["base_health"] + random.randrange(1,7)
        self.strength = stats['strength']
        self.intellect = stats['intellect']
        self.dexterity = stats['dexterity']
        self.initiative = stats['initiative']
        self.constitution = stats['constitution']
        self.wisdom = stats['wisdom']

        self.current_health = self.max_health
        self.physical_attack = stats["base_physical_attack"]
        self.magic_attack = stats["base_magic_attack"]
        self.armor = stats["base_armor"]

        self.spells = []

