import Unit

class Priest(Unit):
    def __init__(self, game):
        super().__init__(game)
        self.intellect = 3
        self.strength = 2
        self.constitution = 2
        self.dexterity = 3
        self.initiative = 2
        self.wisdom = 3
        self.base_health = 16
        self.base_physical_attack = 4
        self.base_magic_attack = 6
        self.base_armor = 5

    #### SPELLS GO HERE ####