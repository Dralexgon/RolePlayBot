from Translate import Translate

class Item:

    items = [
        Item("cactus")
    ]

    def __init__(self, name: str):
        self.name = name
    
    @staticmethod
    def get_by_name(name: str):
        for item in Item.items:
            if item.name == name:
                return item