import random
import json
from tracemalloc import take_snapshot
import spells
from spells import Spells


class Char():
    def __init__(self, class_reference, character_type, char_name):

        # self.reference_class_dict = self.access_class_reference()
        self.reference_class_dict = class_reference
        self.name = char_name
        self.type = character_type
        self.initialize_stats()
        self.alive = True

        self.equipment = {'armor' : None, 'weapon': None}

    def initialize_stats(self):

        stats = self.reference_class_dict[self.type]

        self.max_health = stats["base_health"] + random.randrange(1,7)
        self.strength = stats['strength']
        self.intelect = stats['intelect']
        self.dexterity = stats['dexterity']
        self.initiative = stats['initiative']
        self.constitution = stats['constitution']
        self.wisdom = stats['wisdom']

        self.current_health = self.max_health
        self.physical_attack = stats["base_physical_attack"]
        self.magic_attack = stats["base_magic_attack"]
        self.armor = stats["base_armor"]

        self.spells = []


    def equip_item(self, item, swap_out = False):
        # assert item.equipment == True, 'item is not equipment so it may not be equipped'

        equip_type = item.item_type
        if swap_out:
            self.equipment[equip_type] = item
        elif self.equipment[equip_type] == None:
            self.equipment[equip_type] = item
        elif (self.equipment[equip_type] != None) & (swap_out == False):
            print('equipment already equipped in this slot')

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

    def use_spells(self,cast_spell = ""):
        
        spell_results = getattr(Spells,cast_spell)(self)
        self.spell_outcome(spell_results, 'self') #Do self modifications here. Send opponent modifications back to arena class and they will call spell_outcome

        return spell_results

    def spell_outcome(self, spell_results, word):
        for x in spell_results[word].keys():
            A = getattr(self,x)
            setattr(self,x,A+spell_results[word][x])

        if self.current_health > self.max_health:
            self.current_health = self.max_health
        return


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


    def gain_spell(self,spell_string):
        self.spells.append(spell_string)

    def use_spell(self, spell_string, spell_class):
        if spell_string not in self.spells:
            return "Character does not have this spell"

        else:
            return spell_class.spell_lookup(self, spell_string)

