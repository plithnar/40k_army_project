import weapon
import random
import csv

class Vehicle:

    def __init__(self, values):

        #All vehicles have these
        self.name = values[0]
        self.front_armor = eval(values[1])
        self.side_armor = eval(values[2])
        self.rear_armor = eval(values[3])
        self.ballistic_skill = eval(values[4])
        self.hull_points = eval(values[5])
        
        #Only walkers have these
        self.weapon_skill = eval(values[6])
        self.strength = eval(values[7])
        self.initiative = eval(values[8])
        self.attacks = eval(values[9])

        #Vehicles have many weapons...
        self.ranged_weapons = []
        #But have no melee weapons (walkers attack the number of times they can at their strength though)

    def copystr(self):
        message = []
        message.append(self.name)
        message.append(self.front_armor)
        message.append(self.side_armor)
        message.append(self.rear_armor)
        message.append(self.ballistic_skill)
        message.append(self.hull_points)
        message.append(self.weapon_skill)
        message.append(self.strength)
        message.append(self.initiative)
        message.append(self.attacks)
        return message

    def getShotAt(self, enemy_unit):
        #Test for if Enemy actually hits with the shot
        additional_damage = []
        if enemy_unit.shoot:
            ap_roll = random.randint(1,6)
            armor_mod = 0
            if enemy_unit.ranged_weapon.armor_pierce < 3:
                armor_mod = 3 - enemy_unit.ranged_weapon.armor_pierce
            damage_roll = random.randint(1,6)
            strength = enemy_unit.ranged_weapon.strength 
            # For Front Armor
            if strength + armor_mod + ap_roll == self.front_armor:
                self.hull_points -= 1
                #glancing hit
            if strength + armor_mod + ap_roll > self.front_armor:
                #penetrating hit

            # For Side Armor
            if strength + armor_mod + ap_roll == self.side_armor:
                self.hull_points -= 1
                #glancing hit
            if strength + armor_mod + ap_roll > self.side_armor:
                #penetrating hit

            # For Rear Armor
            if strength + armor_mod + ap_roll == self.rear_armor:
                self.hull_points -= 1
                #glancing hit
            if strength + armor_mod + ap_roll > self.rear_armor:
                #penetrating hit

    def sufferGlancingHit(self):
        pass

    def sufferPenetratingHit(self):
        pass
