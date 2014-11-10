import random
import unit

"""
"  Base class for all squads of units. This doesn't include vehicles or walkers
"""
class Squad:

    def __init__(self, values):
        self.units = []
        for name in values[0]:
            self.units.append(unit.PreloadedUnits[name])
        self.point_cost = values[1]
        self.additional_units = values[2] #dic keyed on unit name for  point cost
        self.min_size = values[3]
        self.max_size = values[4]
        self.current_size = self.min_size
        self.ranged_weapons = values[5] # list of 4-ples,  weapon name,
                                                      # size req, 
                                                      # num allowed,
                                                      # point cost
        self.melee_weapons = values #

    def addUnit(self, unit_to_add):
        if self.current_size < self.max_size:
            self.units.append(unit_to_add)
            self.point_cost += self.additional_units[unit_to_add.name]
            self.current_size += 1

    def __str__(self):
        message = ""
        for unit in self.units:
            message += "Name: {0}, wounds: {1}\n".format(unit.name, unit.wounds)
        message += "Squad cost: {}, {} units".format(self.point_cost, self.current_size)
        return message

tacSquad = Squad([["Space Marine", "Space Marine", "Space Marine", "Space Marine", "Space Marine Sergeant"], 90, {"Space Marine": 16}, 5, 10, ""])

print(tacSquad)
print("\nAdded another unit")
tacSquad.addUnit(unit.PreloadedUnits["Space Marine"])
print(tacSquad)
