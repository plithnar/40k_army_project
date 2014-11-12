import random
import unit
import weapon
import csv

"""
"  Base class for all squads of units. This doesn't include vehicles or walkers
"""
class Squad:

    def __init__(self, values):
        self.squad_name = values[0]
        self.squad_type = values[1]
        self.units = []
        unit_list = eval(values[2])
        for member in unit_list:
            number = member[0]
            unit_info = member[1::]
            for i in range(number):
                name = unit_info[0]
                rangedWeapon = unit_info[1]
                meleeWeapon = unit_info[2]
                unit_to_add = unit.PreloadedUnits[name]
                message = []
                message.append(unit_to_add.name)
                message.append(unit_to_add.weapon_skill.__str__())
                message.append(unit_to_add.ballistics_skill.__str__())
                message.append(unit_to_add.strength.__str__())
                message.append(unit_to_add.toughness.__str__())
                message.append(unit_to_add.wounds.__str__())
                message.append(unit_to_add.initiative.__str__())
                message.append(unit_to_add.melee_attacks.__str__())
                message.append(unit_to_add.leadership.__str__())
                message.append(unit_to_add.armor_save.__str__())
                unit_to_add = unit.Unit(message)
                unit_to_add.armRangedWeapon(weapon.ranged_weapons[rangedWeapon])
                unit_to_add.armMeleeWeapon(weapon.melee_weapons[meleeWeapon])
                self.units.append(unit_to_add)
        self.point_cost = eval(values[3])
        self.additional_units = eval(values[4]) #dic keyed on unit name for point cost with default equipment
        self.min_size = eval(values[5])
        self.max_size = eval(values[6])
        self.current_size = self.min_size
        self.ranged_weapons = eval(values[7]) # list of 4-ples,  weapon name,
                                                      # unit name
                                                      # size req, 
                                                      # num allowed,
                                                      # point cost
        self.melee_weapons = eval(values[8]) #

    def addUnit(self, unit_name):
        if self.current_size < self.max_size:
            if unit_name in self.additional_units:
                unit_to_add = unit.PreloadedUnits[unit_name]
                unit_to_add.armRangedWeapon(weapon.ranged_weapons[self.additional_units[unit_name][1]])
                unit_to_add.armMeleeWeapon(weapon.melee_weapons[self.additional_units[unit_name][2]])
                self.units.append(unit_to_add)
                self.point_cost += self.additional_units[unit_name][0]
                self.current_size += 1

    def __str__(self):
        message = ""
        self.units = sorted(self.units, key=lambda unit: unit.name)
        for unit in self.units:
            message += "Name: {0}, wounds: {1}\n".format(unit.name, unit.wounds)
        message += "Squad cost: {}, {} units".format(self.point_cost, self.current_size)
        return message

Squads = {"":""}

squads = open("squads/squads.txt")
reader = csv.reader(squads, delimiter='\t')
for row in reader:
    squad = Squad(row)
    Squads[row[0]] = squad

tacSquad = Squads["Tactical Squad"]

print(tacSquad)
print("\nAdded another unit")
tacSquad.addUnit("Space Marine")
print(tacSquad)
