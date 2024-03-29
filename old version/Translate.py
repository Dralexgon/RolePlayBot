#This the class that will translate the text from the user.

class Translate:

    languageToNum = ["english","french"]
    currentLanguage = languageToNum.index("french")
    constantToLanguage = {
        "FIRE_COUNTRY": ("The Fire Country", "La Terre du Feu"),
        "WATER_COUNTRY": ("The Water Country", "La Terre de l'Eau"),
        "EARTH_COUNTRY": ("The Earth Country", "La Terre de la Terre"),
        "AIR_COUNTRY": ("The Air Country", "La Terre de l'Air"),
        "QUESTION_NAME": ("What is your character's name ?", "Quel est le nom de votre personnage ?"),
        "ALREADY_EXIST": ("This character already exist ! Choose another name.", "Ce personnage existe déjà ! Choisissez un autre nom."),
        "QUESTION_GENRE": ("What is your character's gender ? (male,female,other)", "Quel est le genre de votre personnage ? (mâle, femelle, autre)"),
        "QUESTION_RACE": ("What is your character's race ?", "Quelle est la race de votre personnage ?"),
        "QUESTION_COMBAT_CLASS": ("What is your character combat class ?", "Quelle est la classe de combat de votre personnage ?"),
        "QUESTION_MAGIC_CLASS": ("What is your character magic class ?", "Quelle est la classe de magie de votre personnage ?"),
        "CHARACTER_CREATED": ("Your character has been created !", "Votre personnage a été créé !"),
        "ALREADY_IN_GAME": ("You already have a game in progress ! Use the command `!end_game` to end it.", "Vous avez déjà une partie en cours ! Utilisez la commande `!end_game` pour la terminer."),
        "GAME_CREATED": ("Your game has been created !", "Votre partie a été créée !"),
    }

    @staticmethod
    def get(text):
        return Translate.constantToLanguage[text][Translate.currentLanguage]

    @staticmethod
    def setLanguage(language):
        Translate.currentLanguage = Translate.languageToNum.index(language)
