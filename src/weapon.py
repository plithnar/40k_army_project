"""
" Base class for all weapons
"""
class Weapon:
    """
    " Initializes unit to the generic Space Marine values, which are used as
    " a comparison for all other units.
    """
    def __init__(self, values):
        self.range = values[0]
        self.strength = values[1]
        self.type = values[2]
        self.special = values[3::]

