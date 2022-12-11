#This the part of the RPB, where there isn't any direct interaction with discord. 
#It's the center of the programm with only gameplay aspects.

from random import*

class MaitreDuJeu:
    dictionnaryZonesRewards = dict({ #Dictionnary of all the rewards we can get in a specific region
        "TerreDuFeu" : ["cactus","arbre mort","sable rare","scorpion"]
    })
    async def exploration(zone): #Give a random reward to soemone that explore a region.
        for i in dict.keys():
            if i == zone:
                reward = dict[zone][randint(0,len(dict[zone])-1)]
        return reward
        

