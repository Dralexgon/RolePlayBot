from random import randint

from Translate import Translate

class Region:

    regions = [
        Region(
            Translate.get("country.fire"), [
                Item.get_by_name("cactus"),
            ]),
        Region(
            Translate.get("country.water"), [

            ]),
        Region(
            Translate.get("country.earth"), [

            ]),
        Region(
            Translate.get("country.air"), [

            ]),
    ]

    default = regions[0]

    def __init__(self, name: str, rewards: list(item)):
        self.name = name
        self.rewards = rewards
    
    def get_random_reward(self):
        return self.rewards[randint(0, len(self.rewards) - 1)]