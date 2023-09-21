#It's the center of the program with only gameplay aspects.
#Here, there is no direct interaction with discord.

from Character import Character
from Map import Map

class GameManager:

    #will be empty, it's just for testing purpose
    characters = [Character(645005137714348041, "Predatoria", "Femelle", "DemonBorn", "Assassin_furtif", "🔥")]

    regions = { #Dictionnary of all the rewards we can get in a specific region
        "TerreDuFeu" : ("cactus","arbre mort","sable rare","scorpion")
    }

    @staticmethod
    def add_character(character):
        GameManager.characters.append(character)

    @staticmethod
    def get_character_by_owner_id(id):
        for character in GameManager.characters:
            if character.ownerId == id:
                return character
        return None