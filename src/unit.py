import random
import weapon
"""
" Base class for all humanoid units, not applicable for vehicles
"""
class Unit:
    """
    " Initializes unit to the generic Space Marine values, which are used as
    " a comparison for all other units.
    """
    def __init__(self, values):
        self.name = values[0]
        self.weapon_skill = values[1]
        self.ballistics_skill = values[2]
        self.strength = values[3]
        self.toughness = values[4]
        self.wounds = values[5]
        self.initiative = values[6]
        self.melee_attacks = values[7]
        self.leadership = values[8]
        self.armor_save = values[9]
        self.ranged_weapon = weapon.ranged_weapons[values[10]]
        self.melee_weapon = weapon.melee_weapons[values[11]]

    def armRangedWeapon(self, ranged_weapon):
        self.ranged_weapon = ranged_weapon

    def armMeleeWeapon(self, melee_weapon):
        self.melee_weapon = melee_weapon

    def fireAtEnemy(self, enemy_unit):
        armor_roll = random.randint(1,6)
        if (self.shoot 
            and armor_roll < enemy_unit.armor_save 
            and enemy_unit.damaged(self.ranged_weapon.strength)):
            if self.ranged_weapon.strength >= 2 * enemy_unit.toughness:
                enemy_unit.wounds = 0
                print("Unit insta-gibbed")
            else:
                enemy_unit.wounds -= 1
                print("Enemy damaged, wounds reduced to "+enemy_unit.wounds.__str__())
        if enemy_unit.wounds == 0:
            print("He's dead Jim")
            

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

SpcMarine = Unit(["Space Marine", 4, 4, 4, 4, 1, 4, 1, 8, 3, "Boltgun", ""])
SpcMarineSrg = Unit(["Space Marine Sergeant", 4, 4, 4, 4, 2, 4, 1, 9, 3, "Boltgun", ""])

PreloadedUnits = {"Space Marine" : SpcMarine, "Space Marine Sergeant" : SpcMarineSrg}
