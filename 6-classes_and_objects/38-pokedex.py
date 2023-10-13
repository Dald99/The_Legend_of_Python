class Pokemon:
    def __init__(self, entry, name, type, description, level, region, width, height, is_caught):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.level = level
        self.region = region
        self.width = width
        self.height = height
        self.is_caught = is_caught

    def display_pokemon(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Description: {self.description}")
        print(f"Level: {self.level}")
        print(f"Region: {self.region}")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Is caught: {self.is_caught}")

    def speak(self):
        print(self.name)

    def catch(self):
        self.is_caught = True

    def level_up(self):
        self.level += 1


jigglypuff = Pokemon("001", "Jigglypuff", "Fairy", "Pink and white", 1, "Kanto", 0.5, 0.5, True)
pikachu = Pokemon("025", "Pikachu", "Electric", "Mouse", 1, "Kanto", 0.4, 0.4, False)
bulbasaur = Pokemon("001", "Bulbasaur", "Grass", "Green", 1, "Kanto", 0.4, 0.4, False)
charmander = Pokemon("004", "Charmander", "Fire", "Orange", 1, "Kanto", 0.5, 0.4, False)
squirtle = Pokemon("007", "Squirtle", "Water", "Blue", 1, "Kanto", 0.5, 0.4, False)

jigglypuff.level_up()
jigglypuff.display_pokemon()

pikachu.catch()
pikachu.speak()
