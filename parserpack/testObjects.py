from parserpack.GenerateMap import Map
from parserpack.GenerateBiome import Biome

# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

# Tester for GenerateMap and GenerateBiome

# creating a map object
map1 = Map("nuketown")

# setting the map properties
map1.setSize(50, 50)
map1.setPreBiome("biome2")

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