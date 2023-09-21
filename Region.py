from random import randint

from Translate import Translate

class Region:

    regions = [
        Translate.get("country.fire"),
        Translate.get("country.water"),
        Translate.get("country.earth"),
        Translate.get("country.air"),
    ]

    default = regions[0]

    def __init__(self, name: str, rewards: list(item)):
        self.name = name
        self.rewards = rewards
    
    def get_random_reward(self):
        return self.rewards[randint(0, len(self.rewards) - 1)]