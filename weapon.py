
from unicodedata import name


class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int()
        self.weapons_list = ["Knife", "Fork", "Machete"]