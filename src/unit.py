import random
import weapon
import csv
"""
" Base class for all humanoid units, not applicable for vehicles
"""
class Unit:
    """
    " Initializes unit to the generic Space Marine incoming, which are used as
    " a comparison for all other units.
    """
    def __init__(self, incoming):
            self.name = incoming[0]
            self.weapon_skill = eval(incoming[1])
            self.ballistics_skill = eval(incoming[2])
            self.strength = eval(incoming[3])
            self.toughness = eval(incoming[4])
            self.wounds = eval(incoming[5])
            self.initiative = eval(incoming[6])
            self.melee_attacks = eval(incoming[7])
            self.leadership = eval(incoming[8])
            self.armor_save = eval(incoming[9])
            self.invuln_save = eval(incoming[10])

    def __repr__(self):
        return "Unit({})".format(self.name)
    
    def copystr(self):
        message = []
        message.append(self.name)
        message.append(self.weapon_skill)
        message.append(self.ballistics_skill)
        message.append(self.strength)
        message.append(self.toughness)
        message.append(self.wounds)
        message.append(self.initiative)
        message.append(self.melee_attacks)
        message.append(self.leadership)
        message.append(self.armor_save)
        message.append(self.invuln_save)
        return message

    def armRangedWeapon(self, ranged_weapon):
        self.ranged_weapon = ranged_weapon

    def armMeleeWeapon(self, melee_weapon):
        self.melee_weapon = melee_weapon

    def fireAtEnemy(self, enemy_unit, hit_kill_list):
        for i in self.ranged_weapon.attacks:
            if enemy_unit.wounds != 0:
                armor_roll = random.randint(1,6)
                enemy_save = enemy_unit.armor_save
                if self.ranged_weapon.armor_pierce <= enemy_unit.armor_save:
                    enemy_save = enemy_unit.invuln_save
                if (self.shoot 
                    and armor_roll < enemy_save
                    and enemy_unit.damaged(self.ranged_weapon.strength)):
                    hit_kill_list[0] += 1
                    if self.ranged_weapon.strength >= 2 * enemy_unit.toughness:
                        enemy_unit.wounds = 0
                        print("Unit insta-gibbed")
                    else:
                        enemy_unit.wounds -= 1
                        print("Enemy damaged, wounds reduced to "+enemy_unit.wounds.__str__())
                if enemy_unit.wounds == 0:
                    hit_kill_list[1] += 1
                    print("He's dead Jim")
        return hit_kill_list

    def shoot(self):
        roll = random.randint(1, 6)
        return roll != 1 and roll + self.ballistics_skill > 6

    def damaged(self, inc_str):
        roll = random.randint(1, 6)
        return roll != 1 and roll + inc_str - 4 >= self.toughness

    def meleeHit(self, enemy_unit):
        roll = random.randint(1, 6)
        if roll >= 5:
            return true
        elif roll < 3:
            return false
        elif (enemy_unit.weapon_skill >= self.weapon_skill <= 2*enemy_unit.weapon_skill and
              roll == 4):
            return true
        elif (self.weapon_skill > enemy_unit.weapon_skill and roll == 3):
            return true 
        

    def meleeFight(self, enemy_unit):
        if enemy_unit.initiative > self.initiative:
            if enemy_unit.meleeHit(enemy_unit, self) and self.damaged(self, enemy_unit.melee_weapon.strength):
                if self.instaKill(self, enemy_unit.melee_weapon.strength):
                    self.wounds = 0
                else:
                    self.wounds -= 1
        if self.wounds > 0 and self.meleeHit(self, enemy_unit) and enemy_unitdamaged(enemy_unit, self.melee_weapon.strength):
            if enemy_unit.instaKill(enemy_unit, self.melee_weapon.strength):
                enemy_unit.wounds = 0
            else:
                enemy_unit.wounds -= 1

PreloadedUnits = {"":""}

units = open("units/units.txt")
reader = csv.reader(units)
for row in reader:
    unit = Unit(row)
    PreloadedUnits[row[0]] = unit
