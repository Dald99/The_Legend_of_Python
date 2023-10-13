class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


london = City("London", "UK", 8000000,  ["Big Ben", "Tower Bridge"])
paris = City("Paris", "France", 2000000, ["Eiffel Tower", "Louvre Museum"])
rome = City("Rome", "Italy", 2500000, ["Colosseum", "Pantheon"])
mexico_city = City("Mexico City", "Mexico", 1500000, ["Taj Mahal", "Museo del Prado"])


print(vars(london))
print(vars(paris))
print(vars(rome))
print(vars(mexico_city))

