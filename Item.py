from Translate import Translate

class Item:

    items = [
        Item(Translate.get("item.cactus"))
    ]

    def __init__(self, name: str):
        self.name = name