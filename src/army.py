# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:01:26 2014

@author: plithnar
"""
import squad
import unit
import weapon
import vehicle
import csv

validArmies = ["Space Marine"]

class Army:
    def __init__(self, value):
        if value not in validArmies:
            raise Exception("Must be a valid army")
        self.race = value
        self.hq = []
        self.troop = []
        self.heavy = []
        self.fast = []
        self.elite = []

    def __str__(self):
        s = ""
        s += self.race + "\n"
        if self.hq != []:
            s += "\n" + "HQ units" + "\n"
            for hq in self.hq:
                s += hq + "\n"
            s += "\n"

        if self.troop != []:
            s += "\n" + "Troop units" + "\n"
            for troop in self.troop:
                s += troop + "\n"
            s += "\n"


        return s

    def AddHq(self, hqUnit):
        if self.hq != [] and len(self.hq) >= 2:
            raise Exception("Army can only have a max of 2 hq units")
        self.hq.append(hqUnit)

    def AddTroop(self, troopUnit):
        #I think it can only have 4 troop choices...?
        if self.troop != [] and len(self.troop) >= 4:
            raise Exception("Army can only have a max of 4 troop units")
        self.troop.append(troopUnit)

    def AddHeavy(self, hqUnit):
        if self.heavy != [] and len(self.heavy) >= 3:
            raise Exception("Army can only have a max of 3 Heavy Support units")
        self.heavy.append(hqUnit)

    def AddElite(self, hqUnit):
        if self.elite != [] and len(self.elite) >= 3:
            raise Exception("Army can only have a max of 3 Elite units")
        self.elite.append(hqUnit)

    def AddFast(self, hqUnit):
        if self.fast != [] and len(self.fast) >= 3:
            raise Exception("Army can only have a max of 3 Fast Attack units")
        self.fast.append(hqUnit)

    def SaveArmy(self, saveFilePath):
        saveString = self.race + "\n"
        for hq in self.hq:
            print(hq)
            saveString += "HQ\t"
            saveString += hq.squad_name
        print(saveString)

Armies = {"":""}

squads = open("squads/squads.txt")
reader = csv.reader(squads, delimiter='\t')
for row in reader:
    if row[0] not in Armies and row[0] in validArmies:
        army = Army(row[0])
        Armies[row[0]] = army
    if row[2] == "Troop":
        Armies[row[0]].troop.append(row[1])
    if row[2] == "HQ":
        Armies[row[0]].hq.append(row[1])
    if row[2] == "Elite":
        Armies[row[0]].elite.append(row[1])
    if row[2] == "Heavy Support":
        Armies[row[0]].heavy.append(row[1])
    if row[2] == "Fast Attack":
        Armies[row[0]].fast.append(row[1])



squads = open("vehicles/vehicles.txt")
reader = csv.reader(squads, delimiter='\t')
for row in reader:
    if row[0] not in Armies and row[0] in validArmies:
        army = Army(row[0])
        Armies[row[0]] = army
    if row[2] == "Troop":
        Armies[row[0]].troop.append(row[1])
    if row[2] == "HQ":
        Armies[row[0]].hq.append(row[1])
    if row[2] == "Elite":
        Armies[row[0]].elite.append(row[1])
    if row[2] == "Heavy Support":
        Armies[row[0]].heavy.append(row[1])
    if row[2] == "Fast Attack":
        Armies[row[0]].fast.append(row[1])
#print(Armies)
