import Unit

class Knight(Unit):
    def __init__(self, game):
        super().__init__(game)
        self.intellect = 3
        self.strength = 5
        self.constitution = 4
        self.dexterity = 3
        self.initiative = 3
        self.wisdom = 2
        self.base_health = 20
        self.base_physical_attack = 4
        self.base_magic_attack = 1
        self.base_armor = 5

    #### SPELLS GO HERE ####