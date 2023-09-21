#It's the center of the program with only gameplay aspects.
#Here, there is no direct interaction with discord.

from Character import Character
from Region import Region
from Item import Item
from Translate import Translate
#from Map import Map

class GameManager:

    characters = [Character(645005137714348041, "Predatoria", "Femelle", "DemonBorn", "Assassin_furtif", "🔥")]

    def __init__(self):
        #will be empty, it's just for testing purpose
        self.items = [
            Item("cactus")
        ]
        self.regions = [
            Region(
                Translate.get("country.fire"), [
                    self.items[0],#cactus
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

    def get_item_by_name(self, name: str):
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    @staticmethod
    def add_character(character):
        characters.append(character)

    @staticmethod
    def get_character_by_owner_id(id):
        for character in GameManager.characters:
            if character.ownerId == id:
                return character
        return None