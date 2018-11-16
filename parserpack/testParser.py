from parserpack.MapinatorParser import Parser
# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

# Tester for the MapinatorParser
textFile = open("../MapinatorCode.txt")
ps = Parser()

print()
for line in textFile:
    print("code:", line)
    ps.parse(line)
    print("\n")


