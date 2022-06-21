import random

class char():
    def __init__(self, character_type, char_name):

        self.name = char_name
        self.type = character_type
        self.health_max = 0
        self.initialize_health()
        self.current_health = self.health_max
        

    def initialize_health(self):

        chararacter_health_dict = {'barbarian': 12,
                                    'archer': 7}

        self.health_max = chararacter_health_dict[self.type] + random.randrange(1,7)

