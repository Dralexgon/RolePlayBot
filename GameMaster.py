#This the part of the RPB, where there isn't any direct interaction with discord. 
#It's the center of the programm with only gameplay aspects.

from random import randint

from Character import Character
from Map import Map

class GameMaster:

    characters = [Character(645005137714348041, "Predatoria", "Femelle", "DemonBorn", "Assassin_furtif", "🔥")]

    maps = [
        Map("Arena", "test", [
                    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
                    ["🟩","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","🟩"],
                    ["🟩","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","🟩"],
                    ["🟩","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","🟩"],
                    ["🟩","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","🟩"],
                    ["🟩","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","🟩"],
                    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"]
                ]),
        Map("Arena2", "test", [
                    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
                    ["🟩"," "," "," "," "," "," "," "," ","🟩"],
                    ["🟩"," "," "," "," "," "," "," "," ","🟩"],
                    ["🟩"," "," "," "," "," "," "," "," ","🟩"],
                    ["🟩"," "," "," "," "," "," "," "," ","🟩"],
                    ["🟩"," "," "," "," "," "," "," "," ","🟩"],
                    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"]
                ]),
    ]

    @staticmethod
    def add_character(character):
        GameMaster.characters.append(character)

    @staticmethod
    def get_character_by_owner_id(id):
        for character in GameMaster.characters:
            if character.ownerId == id:
                return character
        return None

    @staticmethod
    def get_map(mapName):
        for map in GameMaster.maps:
            if map.name == mapName:
                return map
        return None


    #TODO finish that later (and understand what it is)
    
    regionsToRewards = { #Dictionnary of all the rewards we can get in a specific region
        "TerreDuFeu" : ("cactus","arbre mort","sable rare","scorpion")
    }

    @staticmethod 
    async def exploration(region): #Give a random reward to someone that explore a region.
        for i in GameMaster.regionsToRewards.keys():
            if i == region:
                reward = GameMaster.regionsToRewards[region][randint(0,len(GameMaster.regionsToRewards[region])-1)]
        return reward