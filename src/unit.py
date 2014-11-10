import random
"""
" Base class for all humanoid units, not applicable for vehicles
"""
class Unit:
    """
    " Initializes unit to the generic Space Marine values, which are used as
    " a comparison for all other units.
    """
    def __init__(self, values):
        self.weapon_skill = values[0]
        self.ballistics_skill = values[1]
        self.strength = values[2]
        self.toughness = values[3]
        self.wounds = values[4]
        self.initiative = values[5]
        self.melee_attacks = values[6]
        self.leadership = values[7]
        self.armor_save = values[8]
        self.ranged_weapon = None
        self.melee_weapon = None

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
