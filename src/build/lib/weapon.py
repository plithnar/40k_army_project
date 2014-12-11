import sys
import csv
from subprocess import call


"""
" Base class for all weapons
"""
class Weapon:
    """
    " Initializes unit to the generic Space Marine values, which are used as
    " a comparison for all other units.
    """
    def __init__(self, values):
        self.range = values[1]
        self.strength = eval(values[2])
        self.armor_pierce = eval(values[3])
        self.type = values[4]
        self.attacks = values[5]
        self.special = values[6::]

ranged_weapons = {"":""}
melee_weapons = {"":""}

ranged = open("weapons/rangedWeapons.txt")
reader = csv.reader(ranged)
for row in reader:
    weapon = Weapon(row)
    ranged_weapons[row[0]] = weapon

melee = open("weapons/meleeWeapons.txt")
reader = csv.reader(melee)
for row in reader:
    weapon = Weapon(row)
    melee_weapons[row[0]] = weapon
