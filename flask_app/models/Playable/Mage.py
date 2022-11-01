import Unit

class Mage(Unit):
    def __init__(self, game):
        super().__init__(game)
        self.intellect = 4
        self.strength = 2
        self.constitution = 2
        self.dexterity = 3
        self.initiative = 5
        self.wisdom = 4
        self.base_health = 14
        self.base_physical_attack = 2
        self.base_magic_attack = 10
        self.base_armor = 3

    #### SPELLS GO HERE ####