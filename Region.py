from random import randint

from Translate import Translate
from Item import Item

class Region:

    def __init__(self, name: str, rewards: list[Item]):
        self.name = name
        self.rewards = rewards

    @staticmethod
    def get_by_name(name: str):
        for region in Region.regions:
            if region.name == name or Translate.get(region.name):
                return region
        return None

    def get_random_reward(self):
        return self.rewards[randint(0, len(self.rewards) - 1)]