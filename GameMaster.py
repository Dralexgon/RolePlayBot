#This the part of the RPB, where there isn't any direct interaction with discord. 
#It's the center of the programm with only gameplay aspects.

from random import randint

class GameMaster:

    characters = []


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