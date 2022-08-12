from character import *
import time
import random
import os
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
        if self.char1.dexterity > self.char2.dexterity:
            first_move = 'char1'
        elif self.char1.dexterity < self.char2.dexterity:
            first_move = 'char2'
        else:
            if random.randint(1,2) == 1:
                first_move = 'char1'
            else:
                first_move = 'char2'

        while self.char1.alive and self.char2.alive:
            print("Initiating Next Round of Combat!")
            char1_move = input("Player 1, which move do you want to use?  Select p for physical or m for magic: ")
            char2_move = input("Player 2, which move do you want to use?  Select p for physical or m for magic: ")
            
            char1_damage_dealt = self.char1.calculate_attack(char1_move) - self.char2.calculate_defense()
            char2_damage_dealt = self.char2.calculate_attack(char2_move) - self.char1.calculate_defense()

            if first_move == 'char1':
                self.char2.take_damage(char1_damage_dealt)
                if self.char2.alive:
                    self.char1.take_damage(char2_damage_dealt)
            elif first_move == 'char2':
                self.char1.take_damage(char2_damage_dealt)
                if self.char1.alive:
                    self.char2.take_damage(char1_damage_dealt)


            print("Char 1 health remaining: ", self.char1.current_health)
            print("Char 2 health remaining: ", self.char2.current_health)

        #End of Combat
        if not self.char1.alive:
            print("Character 1 has been defeated. Congratulations, character 2!")
        if not self.char2.alive:
            print("Character 2 has been defeated. Congratulations, character 1!")


