from flask_app.models.character import *
import time
import random
import os
import spells
#from Attack_moves import *
import json

#NEED TO TURN THIS INTO A CLASS, SO CHARACTERS CAN FIGHT MULTIPLE TIMES

# #Importing json
# with open("character_class_configs.json") as f:
#     reference_class_dict = json.load(f)
    
# with open('item_config.json') as data_file:
#     item_data = json.load(data_file)


# #Here is where the characters are generated

# char1_name = input("Player 1: What do you want your character's name to be?  ")
# char1_type = input("Player 1: What do you want your character's type to be?  ")
# char1_item = input("Player 1: What do you want your character's item to be?  ")

# char2_name = input("Player 2: What do you want your character's name to be?  ")
# char2_type = input("Player 2: What do you want your character's type to be?  ")
# char2_item = input("Player 2: What do you want your character's item to be?  ")

# char1 = char(reference_class_dict, char1_type, char1_name)
# char2 = char(reference_class_dict, char2_type, char2_name)

#NEED TO ADD ITEMS







class Arena:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    
    def combat(self):
        #Combat happens
        
        #initial combat - choose most dexterous to go first
        if self.char1.initiative > self.char2.initiative:
            first_move = 'char1'
        elif self.char1.initiative < self.char2.initiative:
            first_move = 'char2'
        else:
            if random.randint(1,2) == 1:
                first_move = 'char1'
            else:
                first_move = 'char2'

        print(f'Character Stats:\n {self.char1.name}: {self.char1.char_summary()}\n {self.char2.name}: {self.char2.char_summary()}  ')

        while self.char1.alive and self.char2.alive:
            char1_damage_dealt = 0
            char2_damage_dealt = 0
            
            print("\nInitiating Next Round of Combat!")
            char1_move = input(f"{self.char1.name}, do you want to use an attack or a spell? 'a' = attack; 's' = spell, 'end' to exit combat: ")
            if char1_move == 'end':
                break
            elif char1_move == 'a':
                char1_move = input(f"{self.char1.name}, which move do you want to use?  Select p for physical, m for magic: ")
                char1_damage_dealt = self.char1.calculate_attack(char1_move) - self.char2.calculate_defense()

            elif char1_move == 's':
                print("List of spells: ")
                char1_move = input(f"{self.char1.name}, which spell do you want to use? ")    
                spell_results = self.char1.use_spells(char1_move)
                self.char2.spell_outcome(spell_results,'opponent')

            
            char2_move = input(f"{self.char2.name}, do you want to use an attack or a spell? 'a' = attack; 's' = spell; 'end' to exit combat: ")
            if char2_move == 'end':
                break
            elif char2_move == 'a':
                char2_move = input(f"{self.char2.name}, which move do you want to use?  Select p for physical, m for magic: ")
                char2_damage_dealt = self.char2.calculate_attack(char2_move) - self.char1.calculate_defense()

            elif char2_move == 's':
                print("List of spells: ")
                char2_move = input(f"{self.char1.name}, which spell do you want to use? ")    
                spell_results = self.char2.use_spells(char2_move)
                self.char1.spell_outcome(spell_results,'opponent')
                


            if first_move == 'char1':
                self.char2.take_damage(char1_damage_dealt)
                if self.char2.alive:
                    self.char1.take_damage(char2_damage_dealt)
            elif first_move == 'char2':
                self.char1.take_damage(char2_damage_dealt)
                if self.char1.alive:
                    self.char2.take_damage(char1_damage_dealt)


            print(f'{self.char1.name} {self.char1.char_summary()}')
            print(f'{self.char2.name} {self.char2.char_summary()}')

        #End of Combat
        if not self.char1.alive:
            print(self.char1.name," has been defeated. Congratulations, ", self.char2.name)
        if not self.char2.alive:
            print(self.char2.name, " has been defeated. Congratulations, ",self.char1.name)


