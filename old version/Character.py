class Character:

    def __init__(self, ownerId: int, surname: str, gender: str, race: str, combatClass: str, magicClass: str, firstname: str = "default", lastname: str = "default", age: int = 25, height: int = 175, weight: int = 70):
        self.ownerId = ownerId
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
        self.combatClass = combatClass
        self.magicClass = magicClass
        self.health = 100
        self.maxHealth = 100
        self.mana = 100
        self.maxMana = 100
        self.stamina = 100
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.wisdom = 10
        self.charisma = 10
        self.constitution = 10
        self.luck = 10
        self.inventory = []
        self.equipped = []
        self.gold = 0
        self.xp = 0
        self.level = 1
        self.abilities = []
        self.spells = []
    
    def get_profile_card(self) -> str:
        card = "## Character profile card :\n"
        card += "### Character permanent information (lore) :\n\n"
        card += "- Name: " + self.surname + "\n"
        card += "- Race: " + self.race + "\n"
        card += "- Gender: " + self.gender + "\n"
        card += "- Age: " + str(self.age) + "\n"
        card += "- Height: " + str(self.height // 100) + "m" + str(self.height % 100) + "\n"
        card += "- Weight: " + str(self.weight) + "kg" + "\n"
        card += "- Combat Class: " + self.combatClass + "\n"
        card += "- Magic Class: " + self.magicClass + "\n"

        card += "### Character ?????? :\n\n"

        card += "- Level: " + str(self.level) + "\n"
        card += "- XP: " + str(self.xp) + "\n"

        card += "### Character ?????? :\n\n"

        card += "- Health: " + str(self.health) + "/" + str(self.maxHealth) + "\n"
        card += "- Mana: " + str(self.mana) + "/" + str(self.maxMana) + "\n"

        card += "### Character statistics :\n\n"

        card += "- Stamina: " + str(self.stamina) + "\n"
        card += "- Strength: " + str(self.strength) + "\n"
        card += "- Intelligence: " + str(self.intelligence) + "\n"
        card += "- Dexterity: " + str(self.dexterity) + "\n"
        card += "- Wisdom: " + str(self.wisdom) + "\n"
        card += "- Charisma: " + str(self.charisma) + "\n"
        card += "- Constitution: " + str(self.constitution) + "\n"
        card += "- Luck: " + str(self.luck) + "\n"

        return card #line 69 <_< (nice)