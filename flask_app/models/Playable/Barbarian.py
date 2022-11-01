import Unit

class Barbarian(Unit):
    def __init__(self, player_name, game):
        super().__init__(game)
        self.intellect = 2
        self.strength = 4
        self.constitution = 4
        self.dexterity = 2
        self.initiative = 2
        self.wisdom = 1
        self.base_health = 24
        self.base_physical_attack = 6
        self.base_magic_attack = 2
        self.base_armor = 3
        self.player_name = player_name

    #### SPELLS GO HERE ####