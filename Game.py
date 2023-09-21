from Character import Character
from GameManager import GameManager

class Game:

    def __init__(self, gameMasterID):
        self.gameMasterID = gameMasterID
        self.playersID = []
        self.playersCharacters = []
        self.map = None

    def add_player(self, playerID):
        self.playersID.append(playerID)
        self.playersCharacters.append(GameManager.get_character_by_owner_id(playerID))