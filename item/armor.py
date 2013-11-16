ARMOR_TYPE_METAL = "Metal"
ARMOR_TYPE_LEATHER = "Leather"

class Armor(object):
    def __init__(self, name, defense, patches=None):
        self._name = name
        self._defense = defense
        self._patches = patches