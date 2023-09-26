from random import randint

from Translate import Translate
from Item import Item

class Region:

    def __init__(self, name: str, loots: list[Item]):
        self.name = name
        self.loots = loots

    @staticmethod
    def get_by_name(name: str):
        for region in Region.regions:
            if region.name == name or Translate.get(region.name):
                return region
        return None

    def get_random_reward(self):
        return self.loots[randint(0, len(self.loots) - 1)]