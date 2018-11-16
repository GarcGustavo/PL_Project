from parserpack.GenerateBiome import Biome
# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

class Map:

    # Instance Variables:
    # name
    # sizeX
    # sizeY
    # biomes --> Array

    # Constructor:
    def __init__(self, name):
        self.name = name
        self.biomes = []

    # Methods:
    def setSize(self, x, y):
        self.sizeX = x
        self.sizeY = y

    def setPreBiome(self, name):
        biome = Biome(name)
        biome.setColor("blue", 100)
        biome.setElevationFreq(500)
        biome.setSeed(1)

        self.biomes.append(biome)

    def setBiome(self, biome):
        self.biomes.append(biome)

    def generateCode(self):
        print("Code Generated....")

    def showProperties(self):
        print("\n***********************************")
        print("MAP PROPERTIES:")

        print("\nName:", self.name)
        print("Size: x =", self.sizeX, ", y =", self.sizeY)

        print("\nBiome lists:")
        for biome in self.biomes:
            print()
            biome.showProperties()

        print("\nEND OF PROPERTIES")
        print("\n***********************************")