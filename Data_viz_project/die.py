from random import randint


class Die(object):
    """One Die simulate"""

    def __init__(self, num_sides=6):
        "Assume a six-sided die."
        self.num_sides = num_sides

    def roll(self):
        "Return a radndom value between 1 and num_sides"
        return randint(1, self.num_sides)
