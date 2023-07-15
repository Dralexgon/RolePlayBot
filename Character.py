class Character:

    def __init__(self, ownername: int, surname: str, gender: int, race: str, combatClass: str, magicClass: str, firstname: str = "default", lastname: str = "default", age: int = 25, height: int = 175, weight: int = 70):
        self.ownername = ownername
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
        self.mana = 100
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