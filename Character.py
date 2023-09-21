from Region import Region

class Character:

    def __init__(self, 
                ownerId: int,
                surname: str,
                gender: str,
                race: str,
                combatClass: str,
                magicClass: str,
                firstname: str = "default",
                lastname: str = "default",
                age: int = 25,
                height: int = 175,
                weight: int = 70):
        
        #technical
        self.ownerId = ownerId

        #lore
        self.surname = surname
        self.firstname = firstname
        self.lastname = lastname
        if firstname == "default": self.firstname = surname
        if lastname == "default": self.lastname = surname
        self.race = race
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.history = Translate.get("character_creation.unknow_history")

        #classes
        self.combatClass = combatClass
        self.magicClass = magicClass

        #statistics
        self.stamina = 100
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.wisdom = 10
        self.charisma = 10
        self.constitution = 10
        self.luck = 10

        #storage
        self.inventory = []
        self.equipped = []
        self.gold = 0

        #experience
        self.xp = 0
        self.level = 0

        #actions
        self.abilities = []
        self.spells = []

        #temporary information
        self.region = Region.default
        self.health = 100
        self.mana = 100
        self.maxHealth = 100
        self.maxMana = 100
    
    def get_profile_card(self) -> str:
        card = "# Character profile card :\n"
        card += "## Permanent information (lore) :\n\n"

        card += "- Name: " + self.surname + "\n"
        card += "- Race: " + self.race + "\n"
        card += "- Gender: " + self.gender + "\n"
        card += "- Age: " + str(self.age) + "\n"
        card += "- Height: " + str(self.height // 100) + "m" + str(self.height % 100) + "\n"
        card += "- Weight: " + str(self.weight) + "kg" + "\n"
        card += "- Combat Class: " + self.combatClass + "\n"
        card += "- Magic Class: " + self.magicClass + "\n"
        card += "- History: " + self.history

        card += "## Not permanent information :\n\n"

        card += "### Statistics :\n\n"

        card += "- Stamina: " + str(self.stamina) + "\n"
        card += "- Strength: " + str(self.strength) + "\n"
        card += "- Intelligence: " + str(self.intelligence) + "\n"
        card += "- Dexterity: " + str(self.dexterity) + "\n"
        card += "- Wisdom: " + str(self.wisdom) + "\n"
        card += "- Charisma: " + str(self.charisma) + "\n"
        card += "- Constitution: " + str(self.constitution) + "\n"
        card += "- Luck: " + str(self.luck) + "\n"

        card += "### Experience :\n\n"

        card += "- Level: " + str(self.level) + "\n"
        card += "- XP: " + str(self.xp) + "\n"

        card += "### Storage :\n\n"

        card += "Inventory :" + self.inventory + "\n"
        card += "Equipped :" + self.inventory + "\n"
        card += "Gold :" + self.gold + "\n"

        card += "### Action :\n\n"

        card += "Abilities :" + self.abilities + "\n"
        card += "Spells :" + self.spells + "\n"

        card += "### Fighting information :\n\n"

        card += "- Health: " + str(self.health) + "/" + str(self.maxHealth) + "\n"
        card += "- Mana: " + str(self.mana) + "/" + str(self.maxMana) + "\n"

        return card