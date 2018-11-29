import ply.lex as lex

# Mapinator Project
# Members:
# Jamel Peralta
# Gustavo Reyes
# Alejandro Matos
# Antonio

tokens = (
    'RESERVED',
    'NAME',
    'NUMBER',
    'DECIMAL',
)

t_ignore = ' \t'

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DECIMAL = r'[.][0-9]*'

t_RESERVED = r'GenerateCode | GenerateMap | SetMapSize | SetSeed | SetLacunarity | SetDetails | SetHeightMult | SetNoiseScale | SetNoiseDensity | SetPersistance'

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t) :
    raise SyntaxError("syntax error on line %d near '%s'" %
    (t.lineno, t.value))

lexer = lex.lex()

###########################################################
# TESTER

content = ""

codeText = open("MapinatorCode.txt")
content = codeText.read()

# Give the lexer some input
lexer.input(content)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
