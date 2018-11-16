import ply.lex as lex

tokens = (
    'RESERVED',
    'NAME',
    'NUMBER',
    'DECIMAL',
    'PLUS',
    'MINUS',
    'TIME',
    'DIVIDE',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    'LKEYBRACKET',
    'RKEYBRACKET',
    'LSBRACKET',
    'RSBRACKET'
)

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIME = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'\='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_LKEYBRACKET = r'\{'
t_RKEYBRACKET = r'\}'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'
t_DECIMAL = r'[.][0-9]*'

t_RESERVED = r'GenerateMap | SetMapSize | GenerateBiome | SetBiome | ModBiome | Seed | Color | ElevationFreq'

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
