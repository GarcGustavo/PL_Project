from parserpack.GenerateMap import Map
from parserpack.GenerateBiome import Biome

# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

# Mapinator Parser
class Parser:

    # INSTANCE VARIABLES:
    # map
    # biomes
    # preSetBiomes

    # CONSTRUCTOR:
    def __init__(self):
        self.biomes = []
        self.preSetBiomes = []

        # set preset-Biomes
        self.preSetBiomes.append("biome2")


    # METHODS:

    # parsing the line of code
    def parse(self, lineCode):
        # getting the command from the line string in file
        lineCode = lineCode.replace("\n", "")
        words = lineCode.split(" ")
        command = words[0]

        # pointing the string command to their respects functions
        if command == "GenerateMap":
            self.generateMap(words)
        elif command == "SetMapSize":
            self.setMapSize(words)
        elif command == "SetSeed":
            self.setSeed(words)
        elif command == "SetLacunarity":
            self.setLacunarity(words)
        elif command == "SetDetails":
            self.setDetails(words)
        elif command == "SetHeightMult":
            self.setHeightMult(words)
        elif command == "SetNoiseScale":
            self.setNoiseScale(words)
        elif command == "SetNoiseDensity":
            self.setNoiseDensity(words)
        elif command == "SetPersistance":
            self.setPersistance(words)
        elif command == "GenerateCode":
            self.generateCode()



        # if biome is created.
        elif command == "SetBiome":
            self.setBiome(words)
        elif command == "GenerateBiome":
            self.generateBiome(words)
        elif command == "ModBiome":
            parameter = words[2]
            if parameter == "Seed":
                self.modBiomeSeed(words)
            elif parameter == "Colors":
                self.modBiomeColors(words)
            elif parameter == "ElevationFreq":
                self.modBiomeElevation(words)

    # GenerateMap map_name
    def generateMap(self, words):
        print("map generated")

        # parameters
        name = words[1]

        # generate map
        self.map = Map(name)

    # SetMapSize map_name x y
    def setMapSize(self, words):
        print("setting the map size")

        # parameters
        mapName = words[1]
        x = int(words[2])
        y = int(words[3])

        # setting the size into the map
        self.map.setSize(x, y)

    # SetSeed map_name (0-1)
    def setSeed(self, words):
        print("setting the seed")

        # parameters
        seed = int(words[2])

        # setting the seed into map
        self.map.setSeed(seed)

    # SetLacunarity map_name frequency_value
    def setLacunarity(self, words):
        print("setting the lacunarity")

        # parameters
        value = int(words[2])

        # setting the lacunarity into map
        self.map.setLacunarity(value)

    # SetDetails map_name (0-6)
    def setDetails(self, words):
        print("setting the details")

        # parameters
        value = int(words[2])

        # setting the details into map
        self.map.setDetails(value)

    # SetHeightMult map_name (0-20)
    def setHeightMult(self, words):
        print("setting the height multiplier")

        # parameters
        value = int(words[2])

        # setting the height mult into map
        self.map.setHeightMultiplier(value)

    # SetNoiseScale map_name (0-30)
    def setNoiseScale(self, words):
        print("setting the noise scale")

        # parameters
        value = int(words[2])

        # setting the noise scale into map
        self.map.setNoiseScale(value)

    # SetNoiseDensity map_name (0-10)
    def setNoiseDensity(self, words):
        print("setting the noise density")

        # parameters
        value = int(words[2])

        # setting the noise density into map
        self.map.setNoiseDensity(value)

    # SetPersistance map_name (0-1)
    def setPersistance(self, words):
        print("setting the persistance")

        # parameters
        value = int(words[2])

        # setting the persistance into map
        self.map.setPersistance(value)

    # GenerateCode map_name
    def generateCode(self):
        self.map.showMap()
        self.map.generateCode()


    # ************* METHODS FOR BIOMES (if applied) ***************

    # check if biome exist or not
    def biomeExist(self, biomeName):
        for biome in self.biomes:
            if biome.name == biomeName:
                return 1
        return 0

    # finding a specific biome in the biome list and return it
    def findBiome(self, biomeName):
        for biome in self.biomes:
            if biome.name == biomeName:
                return biome

    # SetBiome map_name biome_name
    def setBiome(self, words):
        print("Setting a biome to map")

        # parameters
        mapName = words[1]
        biomeName = words[2]

        # checking if biome is a preset
        exist = 0
        for pBiome in self.preSetBiomes:
            if pBiome == biomeName:
                exist = 1

        if exist:
            self.map.setPreBiome(biomeName)
        else:
            # There is not a preset for this biome
            biome = self.findBiome(biomeName)
            self.map.setBiome(biome)

    # GenerateBiome biome_name
    def generateBiome(self, words):
        print("generating a new biome from scratch")

        # parameter
        biomeName = words[1]

        # checking the biome exist
        if self.biomeExist(biomeName):
            print("Error: A biome already exist with that name")
        else:
            biome = Biome(biomeName)
            self.biomes.append(biome)


    # GenerateBiome biome_name Seed (0-1)
    def modBiomeSeed(self, words):
        print("setting the biome seed")

        # parameter
        biomeName = words[1]
        seed = int(words[3])
        print("biome:", biomeName, "seed", seed)

        # finding biome and setting the seed
        biome = self.findBiome(biomeName)
        biome.setSeed(seed)

    # ModBiome biome_name Colors color1 color_height
    def modBiomeColors(self, words):
        print("setting the biome colors")

        # parameter
        biomeName = words[1]
        color = words[3]
        height = int(words[4])

        # finding biome and setting the color with his height
        biome = self.findBiome(biomeName)
        biome.setColor(color, height)

    # ModBiome biome_name ElevationFreq freq
    def modBiomeElevation(self, words):
        print("setting the biome elevation")

        # parameter
        biomeName = words[1]
        freq = int(words[3])

        # finding biome and setting the elevation frequency
        biome = self.findBiome(biomeName)
        biome.setElevationFreq(freq)

