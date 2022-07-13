from character.py import *
import time
import random
import os
from Attack_moves.py import *

#Here is where the characters are generated

char1_name = input("Player 1: What do you want your character's name to be?  ")
char1_type = input("Player 1: What do you want your character's type to be?  ")

char2_name = input("Player 2: What do you want your character's name to be?  ")
char2_type = input("Player 2: What do you want your character's type to be?  ")

char1 = character(char1_type, char1_name)
char2 = character(char2_type, char2_name)



    #Print information for each player here

    # attack1a = random.randint(1000,9999)
    # attack1b = random.randint(1000,9999)
    # attack1c = random.randint(1000,9999)
    # attack1d = random.randint(1000,9999)
    # attack1e = random.randint(1000,9999) #may have duplicate numbers - need to consider this

    # print("Only Player 1 should look at the screen. Please take a screenshot. This information will disappear in 5 seconds.")
    # print("Your max health is :",char1.health_max,"\n")
    # print("Your weapon is: ", char1.weapon1)
    # print(f"Your attack codes are: \n water attack: {attack1a}\n air attack: {attack1b}\n earth attack: {attack1c}\n fire attack: {attack1d}\n weapon attack: {attack1e}\n")

    # time.sleep(5)
    # os.system('clear')


    # attack2a = random.randint(1000,9999)
    # attack2b = random.randint(1000,9999)
    # attack2c = random.randint(1000,9999)
    # attack2d = random.randint(1000,9999)
    # attack2e = random.randint(1000,9999) #may have duplicate numbers - need to consider this

    # print("Only Player 2 should look at the screen. Please take a screenshot. This information will disappear in 5 seconds.")
    # print("Your max health is :",char2.health_max,"\n")
    # print("Your weapon is: ", char2.weapon1)
    # print(f"Your attack codes are: \n water attack: {attack2a}\n air attack: {attack2b}\n earth attack: {attack2c}\n fire attack: {attack2d}\n weapon attack: {attack2e}\n")

    # time.sleep(5)
    # os.system('clear')


    #Combat happens
    # while char1.current_health > 0 and char2.current_health > 0:
    #     print("Hi")
    #     char1_attack = int(input("Character 1, which attack do you want to use? Enter code: "))
    #     char2_attack = int(input("Character 2, which attack do you want to use? Enter code: "))
    #     char1_attack = translate_attack(char1_attack, attack1a, attack1b, attack1c, attack1d, attack1e)
    #     char2_attack = translate_attack(char2_attack, attack2a, attack2b, attack2c, attack2d, attack2e)

    #     char1_damagedealt = char1 
    #     char1.current_health -= 1
    #     char2.current_health -= 1


#Combat happens
while char1.current_health > 0 and char2.current_health > 0:
    print("Initiating Next Round of Combat!")
    char1_attack = int(input("Character 1, which attack do you want to use? Enter p for physical or m for magic: "))
    os.system('clear')
    char2_attack = int(input("Character 1, which attack do you want to use? Enter p for physical or m for magic: "))
    os.system('clear')

    #Lines 82 - 96 (if statements) should be character functions, and output damage returned to arena
    # if char1_attack == "p":
    #     damage = char1.physical_attack
    # else:
    #     damage = char1.magic_attack #This means code will default to magic if any other thing is written

    # char1_damagedealt = damage + char1_weapon_damage - char2.armor 

    # if char2_attack == "p":
    #     damage = char2.physical_attack
    # else:
    #     damage = char2.magic_attack #This means code will default to magic if any other thing is written

    # char2_damagedealt = damage + char2_weapon_damage - char1.armor

    char2.current_health -= char1.damage_dealt #damage done to character 2
    char1.current_health -= char2.damage_dealt #damage done to character 1
    print("Char 1 health remaining: ", char1.current_health)
    print("Char 2 health remaining: ", char2.current_health)

#End of Combat
if char1.current_health <= 0:
    print("Character 1 has been defeated. Congratulations, character 2!")
if char2.current_health <= 0:
    print("Character 2 has been defeated. Congratulations, character 1!")