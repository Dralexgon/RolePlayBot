class Map:
    
    def __init__(self, name, description, matrix):
        self.name = name
        self.description = description
        self.matrix = matrix
    
    def __str__(self):
        return self.name + " : " + self.description
    
    def get_image(self):
        image = "```"
        for row in self.matrix:
            for char in row:
                image += char
            image += "\n"
        return image + "```"