# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:01:26 2014

@author: plithnar
"""

#pylint: disable=C0103

validArmies = ["Chaos", "Eldar", "Tau", "Ork", "Space Marine",
                 "Imperial Guard", "Tyranid"]

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
        if self.hq != [] and self.hq.count >= 2:
            raise Exception("Army can only have a max of 2 hq units")
        self.hq.append(hqUnit)

    def AddTroop(self, troopUnit):
        #I think it can only have 4 troop choices...?
        if self.troop != [] and self.troop.count >= 4:
            raise Exception("Army can only have a max of 2 hq units")
        self.troop.append(troopUnit)

print test
