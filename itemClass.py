
class item():
    def __init__(self, name, item_stats):
        self.name = name
        self.item_type = item_stats["item_type"]
        self.damage = item_stats["damage"]
        self.defense = item_stats["defense"]
        self.imbue = item_stats["imbue"]
        self.magic_damage = item_stats["magic_damage"]
