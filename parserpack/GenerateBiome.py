# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

class Biome:

    # Instance Variables:
    # name
    # heights ---> list
    # elevationFreq
    # seed
    # colors ----> list

    # Constructor:
    def __init__(self, name):
        self.name = name
        self.colors = []
        self.heights = []

    # Methods:
    def setElevationFreq(self, freq):
        self.elevationFreq = freq

    def setSeed(self, seed):
        self.seed = seed

    def setColor(self, color, height):
        self.colors.append(color)
        self.heights.append(height)

    def showProperties(self):
        print("Biome Properties:")
        print("Name:", self.name)
        print("Seed:", self.seed)
        print("Elevation Frequency:", self.elevationFreq)
        print("Colors of elevation:")
        for i, color in enumerate(self.colors):
            print("color:", color, "and height:", self.heights[i])