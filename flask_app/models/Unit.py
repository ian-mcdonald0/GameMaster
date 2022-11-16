import random
import flask_app.models.spells as spells
from flask_app.models.spells import spells

# Parent class for all units in game
class Unit():
    def __init__(self, game):
        self.intellect = 1
        self.strength = 1
        self.constitution = 1
        self.dexterity = 1
        self.initiative = 1
        self.wisdom = 1
        self.base_health = 1
        self.base_physical_attack = 1
        self.base_magic_attack = 1
        self.base_armor = 1
        self.alive = True
        self.game = game


    #### ITEM METHODS ####
    def equip_item(self, item, swap_out = True):
        equip_type = item.item_type
        if swap_out:
            self.equipment[equip_type] = item
        elif self.equipment[equip_type] == None:
            self.equipment[equip_type] = item
        elif (self.equipment[equip_type] != None) & (swap_out == False):
            print('equipment already equipped in this slot')
        return

    def buy_item(self, coins = 100):
        i = 1
        for item_name in list(self.game.shop.armory.keys()):
            print("The items you can buy are: [", i,"] ",item_name)
            i += 1
        x = int(input(print("What would you like to buy? For none, press 0.")))
        if x != 0:
            bought_item = self.game.shop.purchase_item(list(self.game.shop.armory.keys())[x-1])
            #x = int(input(print("What would you like to buy? For none, press 0.")))
        self.equip_item(bought_item)
        return

    #### DEALING AND RECIEVING DAMAGE ####
    def calculate_attack(self, attack_move):
        if attack_move == 'p':
            attack_dmg = random.randrange(1,6)
            attack_dmg += self.physical_attack
            if self.equipment['weapon'] != None:
                attack_dmg += self.equipment['weapon'].damage
            return attack_dmg
        
        elif attack_move == 'm':
            attack_dmg = random.randrange(1,6)
            attack_dmg += self.magic_attack
            if self.equipment['weapon'] != None:
                attack_dmg += self.equipment['weapon'].magic_damage
            return attack_dmg
    
    def calculate_defense(self):
        if self.equipment['armor'] == None:
            return self.armor
        else:
            return self.armor + self.equipment['armor'].defense

    def take_damage(self, damage):
        if damage < 0:
            damage = 0
        self.current_health = self.current_health - damage
        if self.current_health <= 0:
            self.alive = False
    
    #### SPELL METHODS ####
    def use_spells(self,cast_spell = ""):
        
        spell_results = getattr(spells,cast_spell)(self)
        self.spell_outcome(spell_results, 'self') #Do self modifications here. Send opponent modifications back to arena class and they will call spell_outcome

        return spell_results

    def spell_outcome(self, spell_results, word):
        for x in spell_results[word].keys():
            A = getattr(self,x)
            setattr(self,x,A+spell_results[word][x])

        if self.current_health > self.max_health:
            self.current_health = self.max_health
        return

    def gain_spell(self,spell_string):
        self.spells.append(spell_string)

    def use_spell(self, spell_string, spell_class):
        if spell_string not in self.spells:
            return "Character does not have this spell"
        else:
            return spell_class.spell_lookup(self, spell_string)

    #### GET CHARACTER INFO
    def char_summary(self):

        char_stats = {'current_health': self.current_health,
                        'armor': self.armor,
                        'physical_attack': self.physical_attack,
                        'magic_attack': self.magic_attack,
                        'strength': self.strength,
                        'intellect': self.intellect}

        return char_stats

    #todo add a spell look up