#This the class that will translate the text from the user.

class Translate:

    languageToNum = ["english","french"]
    currentLanguage = languageToNum.index("french")
    constantToLanguage = {
        "FIRE_COUNTRY": ("The Fire Country", "La Terre du Feu"),
        "WATER_COUNTRY": ("The Water Country", "La Terre de l'Eau"),
        "EARTH_COUNTRY": ("The Earth Country", "La Terre de la Terre"),
        "AIR_COUNTRY": ("The Air Country", "La Terre de l'Air")
    }

    @staticmethod
    def get(text):
        return constantToLanguage[text][currentLanguage]

    @staticmethod
    def setLanguage(language):
        currentLanguage = languageToNum.index(language)
