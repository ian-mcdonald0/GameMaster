import Unit

class Archer(Unit):
    def __init__(self, player_name, game):
        super().__init__(game)
        self.intellect = 3
        self.strength = 2
        self.constitution = 2
        self.dexterity = 4
        self.initiative = 3
        self.wisdom = 2
        self.base_health = 16
        self.base_physical_attack = 5
        self.base_magic_attack = 4
        self.base_armor = 3
        self.player_name = player_name

    #### SPELLS GO HERE ####