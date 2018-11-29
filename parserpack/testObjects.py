from parserpack.GenerateMap import Map
from parserpack.GenerateBiome import Biome

# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

# Tester for GenerateMap

# creating a map object
map1 = Map("nuketown")

# setting the map properties
map1.setSize(50, 50)
map1.setSeed(1)
map1.setLacunarity(4)
map1.setDetails(5)
map1.setHeightMultiplier(0)
map1.setNoiseScale(30)
map1.setNoiseDensity(10)
map1.setPersistance(1)

# showing the values
map1.showMap()
map1.generateCode()



# Tester for biome
'''
# creating a custom biome
biome = Biome("biome1")
biome.setElevationFreq(75)
biome.setColor("blue", 10)
biome.setColor("red", 50)
biome.setColor("yellow", 100)
biome.setSeed(0)

# setting the custom biome to the map
map1.setBiome(biome)

# showing all the properties of the map
map1.showProperties()
'''