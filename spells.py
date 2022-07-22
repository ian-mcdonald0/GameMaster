
class Spells():

    def __init__(self):
        self.dummy = None

    def lightining_bolt(character):
        damage = character.magic_attack + 2*character.intelect
        return {"damage": damage}


    def rend(character):
        damage = character.magic_attack + 2*character.intelect
        return {"armor": -2}


    def spell_lookup(character, spell_string):
    
        spell_dict = {'lightning_bolt': lightining_bolt(character),
                        'rend': rend(character)}

        if spell_string in character.spells:
            return spell_dict[spell_string]

        else:
            return 0