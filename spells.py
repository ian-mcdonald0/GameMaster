import random

class Spells():

    def __init__(self):
        self.dummy = None

    def heal2(character):
        heal = random.randrange(10,30)*character.intelect
        return {'self':{"current_health":heal},
                'opponent':{}}

    def heal(self, character):
        return character.health*2
    
    def lightining_bolt(self,character):
        damage = character.magic_attack + 2*character.intelect
        return {'self':{},
                'opponent':{"current_health":damage}}


    def rend(self,character):
        return {'self':{},
        'opponent':{"armor": -2}}


    def spell_lookup(self, character, spell_string):
    
        spell_dict = {'lightning_bolt': self.lightining_bolt(character),
                        'rend': self.rend(character)}

        if spell_string in spell_dict.keys():
            return spell_dict[spell_string]

        else:
            return 0