import random

class Spells():

    def __init__(self):
        self.dummy = None

    def heal(character):
        """
        This spell heals people.
        """
        heal = random.randrange(10,30)*character.intelect
        return {'self':{"current_health":heal},
                'opponent':{}}

    def explosion(character):
        """
        This spell damages your opponent.
        """
        damage = -random.randrange(10,30)*character.intelect
        return {'self':{},
                'opponent':{"current_health":damage},"armor":-2}

    # def stat_booster(character):
    #     """
    #     This spell ups all your stats.
    #     """
    #      = -random.randrange(10,30)*character.intelect
    #     return {'self':{},
    #             'opponent':{"current_health":damage},"armor":-2}

    
    def lightning_bolt(character):
        """
        This spell damages opponents.
        """
        damage = -(character.magic_attack + 2*character.intelect)
        return {'self':{},
                'opponent':{"current_health":damage}}

    def rend(character):
        """
        This spell gets rid of opponents' armor.
        """
        return {'self':{},
                'opponent':{"armor": -2}}


    # def spell_lookup(self, character, spell_string):
    
    #     spell_dict = {'lightning_bolt': self.lightining_bolt(character),
    #                     'rend': self.rend(character)}

    #     if spell_string in spell_dict.keys():
    #         return spell_dict[spell_string]

    #     else:
    #         return 0