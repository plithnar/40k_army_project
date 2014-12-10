import weapon
import random
import squad
import csv

class Vehicle:

    rollToDamageMap = {3:"Crew Stunned", 4:"Weapon Destroyed", 5:"Vehicle Immobilised", 6:"Vehicle Explodes!"}

    def __init__(self, values):
        #All vehicles have these
        self.army_name = values[0]
        self.squad_name = values[1]
        self.squad_type = values[2]
        self.point_cost = eval(values[3])
        self.min_size = eval(values[4])
        self.max_size = eval(values[5])
        self.current_size = self.min_size
        self.front_armor = eval(values[6])
        self.side_armor = eval(values[7])
        self.rear_armor = eval(values[8])
        self.ballistics_skill = eval(values[9])
        self.hull_points = eval(values[10])
        
        #Only walkers have these
        self.weapon_skill = eval(values[11])
        self.strength = eval(values[12])
        self.initiative = eval(values[13])
        self.attacks = eval(values[14])
        self.additional_units = eval(values[15])
        
        self.ranged_weapons = []
        #Vehicles have many weapons...
        for i in range(16, len(values)):
            self.ranged_weapons.append(weapon.ranged_weapons[values[i]])
        #But have no melee weapons (walkers attack the number of times they can at their strength though)

    def addUnit(self, unit_name):
        if self.current_size < self.max_size:
            self.point_cost += int(self.point_cost/self.current_size)
            self.current_size += 1

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
        penHits = 0
        glanceHits = 0
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
                glanceHits += 1
                #glancing hit
            if strength + armor_mod + ap_roll > self.front_armor:
                self.hull_points -= 1
                penHits += 1
                additional_damage.append(self.rollToDamageMap[damage_roll])
                #penetrating hit

            # For Side Armor
            if strength + armor_mod + ap_roll == self.side_armor:
                self.hull_points -= 1
                glanceHits += 1
                #glancing hit
            if strength + armor_mod + ap_roll > self.side_armor:
                self.hull_points -= 1
                penHits += 1
                additional_damage.append(self.rollToDamageMap[damage_roll])
                #penetrating hit

            # For Rear Armor
            if strength + armor_mod + ap_roll == self.rear_armor:
                self.hull_points -= 1
                glanceHits += 1
                #glancing hit
            if strength + armor_mod + ap_roll > self.rear_armor:
                self.hull_points -= 1
                penHits += 1
                additional_damage.append(self.rollToDamageMap[damage_roll])
                #penetrating hit

    def squadFire(self, enemy_squad):
        enemy_units = sorted(enemy_squad.units, key=lambda unit: unit.wounds)
        enemy_size = enemy_squad.current_size
        target = 0
        total_hits_kills = [0, 0]
        for i in range(self.current_size):
            for weapon in self.ranged_weapons:
                if target < enemy_size:
                    self.fireAtEnemy(weapon, enemy_units[target], total_hits_kills)
                    if enemy_units[target].wounds == 0:
                        target += 1
                if target == enemy_size:
                    print("Enemy unit wiped out")
        #print("Hits: {}    Kills: {}".format(total_hits_kills[0], total_hits_kills[1]))
        return (total_hits_kills[0], total_hits_kills[1])

    def fireAtEnemy(self, ranged_weapon, enemy_unit, hit_kill_list):
        for i in ranged_weapon.attacks:
            if enemy_unit.wounds != 0:
                armor_roll = random.randint(1,6)
                enemy_save = enemy_unit.armor_save
                if ranged_weapon.armor_pierce <= enemy_unit.armor_save:
                    enemy_save = enemy_unit.invuln_save
                if (self.shoot 
                    and armor_roll < enemy_save
                    and enemy_unit.damaged(ranged_weapon.strength)):
                    hit_kill_list[0] += 1
                    if ranged_weapon.strength >= 2 * enemy_unit.toughness:
                        enemy_unit.wounds = 0
                    else:
                        enemy_unit.wounds -= 1
                if enemy_unit.wounds == 0:
                    hit_kill_list[1] += 1
        return hit_kill_list

    def shoot(self):
        roll = random.randint(1, 6)
        return roll != 1 and roll + self.ballistics_skill > 6

Vehicles = {}

vehicles = open("vehicles/vehicles.txt")
reader = csv.reader(vehicles, delimiter='\t')
for row in reader:
    vehicle = Vehicle(row)
    Vehicles[row[1]] = vehicle
        
