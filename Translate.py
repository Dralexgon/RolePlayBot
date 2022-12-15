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
        "QUESTION_GENRE": ("What is your character's gender ? (0:boy,1:girl,2:other)", "Quel est le genre de votre personnage ? (0:garçon,1:fille,2:autre)"),
        "QUESTION_RACE": ("What is your character's race ?", "Quelle est la race de votre personnage ?"),
        "QUESTION_COMBAT_CLASS": ("What is your character combat class ?", "Quelle est la classe de combat de votre personnage ?"),
        "QUESTION_MAGIC_CLASS": ("What is your character magic class ?", "Quelle est la classe de magie de votre personnage ?"),
    }

    @staticmethod
    def get(text):
        return Translate.constantToLanguage[text][Translate.currentLanguage]

    @staticmethod
    def setLanguage(language):
        Translate.currentLanguage = Translate.languageToNum.index(language)
