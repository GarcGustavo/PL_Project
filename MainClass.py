from parserpack.MapinatorParser import Parser
from lexerProperties import lexer

# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

# Setting the file, the obj pf parser and the lexer
textFile = open("MapinatorCode.txt")
ps = Parser()

# LEXER: passing the text file to lexer
content = ""
content = textFile.read()

# Give the lexer some input
lexer.input(content)

# Tokenize
print(" ************* LEXER *************")
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

# PARSER: passing the text file to parser
print(" ************* PARSER *************")
textFile = open("MapinatorCode.txt")
for line in textFile:
    print("code:", line)
    ps.parse(line)
    print("\n")