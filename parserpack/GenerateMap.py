from parserpack.GenerateBiome import Biome
import os
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
    # seed
    # lacunarity
    # details
    # heightMult
    # noiseScale
    # noiseDensity
    # persistance
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

    # seed must be between 0 and 1
    def setSeed(self, seed):
        if seed >= 0 and seed <= 1:
            self.seed = seed
        else:
            print("Error: Seed must be from 0 to 1")

    # lacunarity must be from 0 - 5
    def setLacunarity(self, freq):
        if freq >= 0 and freq <= 5:
            self.lacunarity = freq
        else:
            print("Error: lacunarity must be from 0 to 5")

    # details must be from 0-6
    def setDetails(self, detail):
        if detail >= 0 and detail <= 6:
            self.details = detail
        else:
            print("Error: Details value must be from 0 to 6")

    # height multiplier must be from 0 - 20
    def setHeightMultiplier(self, mult):
        if mult >= 0 and mult <= 20:
            self.heightMult = mult
        else:
            print("Error: Height multiplier must be from 0 to 20")

    # noise scale must be from 0 - 30
    def setNoiseScale(self, scale):
        if scale >= 0 and scale <= 30:
            self.noiseScale = scale
        else:
            print("Error: Noise Scale must be from 0 to 30")

    # noise density from 0 - 10
    def setNoiseDensity(self, density):
        if density >= 0 and density <= 10:
            self.noiseDensity = density
        else:
            print("Error: Noise density must be from 0 to 10")

    # persistance from 0 - 1
    def setPersistance(self, persistance):
        if persistance >= 0 and persistance <= 1:
            self.persistance = persistance
        else:
            print("Error: Persistance value must be from 0 to 1")

    # for generating the code in C#
    def generateCode(self):
        import subprocess

        # Setting the path for the input file, output file and the generated project
        inputFile = "input/UnityScripts/Input.txt"
        outputFile = "output/UnityScripts/GenerateMap.cs"

        # Mac Finder
        # projectOutput = "output/UnityScripts"

        # Windows Explorer
        projectOutput = "output"
        path = os.path.realpath(projectOutput)

        # setting the file object with their respect file path
        file = open(inputFile)
        newFile = open(outputFile, "w")

        # for analyzing the old file and generating a new one.
        for line in file:
            if "public string mapName" in line:
                line = line.replace("\n", "")
                line += " = " + '"' + self.name + '"' + ";\n"
                newFile.write(line)
            elif "public int seed" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.seed) + ";\n"
                newFile.write(line)
            elif "public float lacunarity" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.lacunarity) + ";\n"
                newFile.write(line)
            elif "public int editorPreviewLOD" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.details) + ";\n"
                newFile.write(line)
            elif "public float meshHeightMultiplier" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.heightMult) + ";\n"
                newFile.write(line)
            elif "public float noiseScale" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.noiseScale) + ";\n"
                newFile.write(line)
            elif "public int octaves" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.noiseDensity) + ";\n"
                newFile.write(line)
            elif "public float persistance" in line:
                line = line.replace("\n", "")
                line += " = " + str(self.persistance) + ";\n"
                newFile.write(line)
            else:
                newFile.write(line)
            #print(line)

        # for opening in the finder the new project file.

        # Mac Finder
        # subprocess.call(["open", "-R", projectOutput])

        # Windows Explorer
        os.startfile(path)

    def showMap(self):
        print("\n***********************************")
        print("MAP PROPERTIES:")

        print("\nName:", self.name)
        print("Size: x =", self.sizeX, ", y =", self.sizeY)
        print("Seed:", self.seed)
        print("Lacunarity frequency:", self.lacunarity)
        print("Details:", self.details)
        print("Height Multiplier:", self.heightMult)
        print("Noise Scale:", self.noiseScale)
        print("Noise Density:", self.noiseDensity)
        print("Persistance value:", self.persistance)

        print("\nEND OF PROPERTIES")
        print("\n***********************************")






    # METHODS IF BIOMES
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