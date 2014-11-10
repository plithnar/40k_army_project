"""
" Base class for all weapons
"""
class Weapon:
    """
    " Initializes unit to the generic Space Marine values, which are used as
    " a comparison for all other units.
    """
    def __init__(self, values):
        self.range = values[0]
        self.strength = values[1]
        self.armor_pierce = values[2]
        self.type = values[3]
        self.special = values[4::]

boltGun = Weapon([24, 4, 5, "Rapid Fire"])
ranged_weapons = {"Bolt Gun" : boltGun}
melee_weapons = {"" : ""}
