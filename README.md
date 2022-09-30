# GameMaster
our first foray in object oriented game programming


### Game Description
1. PVP Game
2. Each round each player pick an attack style and a defense style (augment to attack and defense)
3. Each player as one attack and one defense
4. Items can modify this

#### Combat rules
1. Certain defense styles are weak and strong against certain attack styles
    a. this will determine what modifier a person receives for damage.
2. combat will be turn based

### Code breakdown
1. Characters
    a. Attack
        1. mana based ?
        2. stam based ?
        3. action point ?
    b. Defense
    c. Hitpoint
    d. Stamina

2. Items
    a. Weapons
    b. Armor
    c. Pots
    d. Misc

3. Monsters
    a. Attack
    b. Defense
    c. Hp
    d. Specials

3. Arena
    a. contains multi chars
    b. contains multi monsters
    c. allows environment for chars and monsters to interact




Shop Class Requirements:
1. Characters need money
2. Characters need to interact with the shop to purchase items
3. When a character purchases an item, character must equip item
4. the shop must take the money
5. the shop must replenish the item?
6. Game class instantiates shop
7. space for characters to interact with shop inside of game class
8. Arena focuses on facilitating fighting.

Class Hierarchy
Game
    Shop - where we get items and spells
    Characters - obvious
    Arena - facilitates fighting
    Items - 


