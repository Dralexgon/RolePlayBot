#This the class that will translate the text from the user.

class Translate:

    languageToNum = ["english","french"]
    currentLanguage = languageToNum.index("french")
    constantToLanguage = {
        "country": {
            "fire": ("The Fire Country", "La Terre du Feu"),
            "water": ("The Water Country", "La Terre de l'Eau"),
            "earth": ("The Earth Country", "La Terre de la Terre"),
            "air": ("The Air Country", "La Terre de l'Air"),
        },
        "character_creation": {
            "question": {
                "name": ("What is your character's name ?", "Quel est le nom de votre personnage ?"),
                "genre": ("What is your character's gender ? (male,female,other)", "Quel est le genre de votre personnage ? (mâle, femelle, autre)"),
                "race": ("What is your character's race ?", "Quelle est la race de votre personnage ?"),
                "combat_class": ("What is your character combat class ?", "Quelle est la classe de combat de votre personnage ?"),
                "magic_class": ("What is your character magic class ?", "Quelle est la classe de magie de votre personnage ?"),
            },
            "already_exist": ("This character already exist ! Choose another name.", "Ce personnage existe déjà ! Choisissez un autre nom."),
            "created": ("Your character has been created !", "Votre personnage a été créé !"),
            "unknow_history": ("History unknow", "Histoire inconnue"),
        },
        "item": {
            "receive": ("You received : ", "Tu as reçu : "),
            "cactus": ("Cactus", "Cactus")
        },
        "error": {
            "no_character": ("You don't have a character yet ! Use !create_character to create one !", "Tu n'as pas de personnage pour l'instant ! Utilise !create_character pour en créer un !")
        }
    }

    @staticmethod
    def get(text):
        try:
            result = Translate.constantToLanguage
            for word in text.split("."):
                result = result[word]
            result = result[Translate.currentLanguage]
            return result
        except:
            return None

    @staticmethod
    def setLanguage(language):
        Translate.currentLanguage = Translate.languageToNum.index(language)
