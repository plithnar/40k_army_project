import random
import unit
import weapon
import csv

"""
"  Base class for all squads of units. This doesn't include vehicles or walkers
"""
class Squad:
    def __init__(self, values):
        self.army_name = values[0]
        self.squad_name = values[1]
        self.squad_type = values[2]
        self.units = []
        unit_list = eval(values[3])
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
                message.append(unit_to_add.invuln_save.__str__())
                unit_to_add = unit.Unit(message)
                unit_to_add.armRangedWeapon(weapon.ranged_weapons[rangedWeapon])
                unit_to_add.armMeleeWeapon(weapon.melee_weapons[meleeWeapon])
                self.units.append(unit_to_add)
        self.point_cost = eval(values[4])
        self.additional_units = eval(values[5]) #dic keyed on unit name for point cost with default equipment
        self.min_size = eval(values[6])
        self.max_size = eval(values[7])
        self.current_size = self.min_size
        self.ranged_weapons = eval(values[8]) # list of 4-ples,  weapon name,
                                                      # unit name
                                                      # size req, 
                                                      # num allowed,
                                                      # point cost
        self.melee_weapons = eval(values[9]) #

    def addUnit(self, unit_name):
        if self.current_size < self.max_size:
            if unit_name in self.additional_units:
                unit_to_add = unit.PreloadedUnits[unit_name]
                unit_to_add.armRangedWeapon(weapon.ranged_weapons[self.additional_units[unit_name][2]])
                unit_to_add.armMeleeWeapon(weapon.melee_weapons[self.additional_units[unit_name][3]])
                self.units.append(unit_to_add)
                self.point_cost += self.additional_units[unit_name][1]
                self.current_size += 1

    def __str__(self):
        message = ""
        self.units = sorted(self.units, key=lambda unit: unit.name)
        for unit in self.units:
            message += "Name: {0}, wounds: {1}\n".format(unit.name, unit.wounds)
        message += "Squad cost: {}, {} units".format(self.point_cost, self.current_size)
        return message

    def squadFire(self, enemy_squad):
        enemy_units = sorted(enemy_squad.units, key=lambda unit: unit.wounds)
        enemy_size = enemy_squad.current_size
        target = 0
        total_hits_kills = [0, 0]
        for unit in self.units:
            if target < enemy_size:
                unit.fireAtEnemy(enemy_units[target], total_hits_kills)
                if enemy_units[target].wounds == 0:
                    target += 1
        if target == enemy_size:
            print("Enemy unit wiped out")
        #print("Hits: {}    Kills: {}".format(total_hits_kills[0], total_hits_kills[1]))
        return (total_hits_kills[0], total_hits_kills[1])

Squads = {"":""}
DefSquads = {}

squads = open("squads/squads.txt")
reader = csv.reader(squads, delimiter='\t')
for row in reader:
    squad = Squad(row)
    Squads[row[1]] = squad

squads = open("squads/defSquads.txt")
reader = csv.reader(squads, delimiter='\t')
for row in reader:
    squad = Squad(row)
    DefSquads[row[1]] = squad

