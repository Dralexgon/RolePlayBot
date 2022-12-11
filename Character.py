class Character:

    def __init__(self, surname: str, firstname: str, lastname: str, race: str, gender: int, age: int, height: int, weight: int, combatClass: str, magicClass: str):
        self.surname = surname
        self.firstname = firstname
        self.lastname = lastname
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