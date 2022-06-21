#Here we will outline the multiplier for each of the four elements
import random
import pandas as pd
import numpy as np

def attack_analysis(attack,defense):
    damage = 0

    multipliers =   [[0.5, 1.5, 0.75 ,2],[1.5, 0.5, 0.75 ,1.25],[1.25, 0.75, 1.25 ,1.5],[0.75, 2, 0.75 ,0.5]]

    damage_multiplier = pd.DataFrame(multipliers,
                  index=pd.Index(['water attack', 'air attack', 'earth attack', 'fire attack'], name='attack'),
                  columns=pd.Index(['water defense', 'air defense', 'earth defense', 'fire defense'], name='defense'))

    print(damage_multiplier)
    print()

    multiplier = damage_multiplier.at[attack, defense]
    return multiplier

mult = attack_analysis("air attack","earth defense")
print(mult)
