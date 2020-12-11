import ply.lex as lex


tokens = ['NUMERO','OPENTAG','CLOSETAG','ID', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',  'EQUALS', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
'COMMA', 'SEMI','LPAREN', 'RPAREN', 'LBRACE', 'RBRACE','DOT','QUOTES','APOSTROPHE']

reservadas = {
# https://dart.dev/guides/language/language-tour#keywords
   'if':'IF',
   'else':'ELSE',
   'null':'NULL',
   'break':'BREAK',
   'true':'TRUE',
   'false':'FALSE',
   'var':'VAR',
   'int':'INT',
   'Void':'VOID',
   'for':'FOR',
   'bool':'BOOL'
}

tokens = tokens + list(reservadas.values())



# RE SYMBOLS
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_LT        = r'<'
t_GT        = r'>'
t_LE        = r'<='
t_GE        = r'>='
t_EQ        = r'=='
t_NE        = r'!='
t_SEMI      = r';'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_DOT       = r'\.'
t_QUOTES    = r'\"'
t_APOSTROPHE = r'\''

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)

def t_NUMBER(t):
    r'\d+\s'
    t.value = int(t.value)
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_espacio(t):
    r"\s"
    pass

# RE OPEN AND CLOSE TAG
def t_OPENTAG(t):
    r'(void\smain\s?\(\))'
    return t

#palabras recervadas

def t_INT(t):
    r'int'
    return t

def t_NUMERO(t):
    r'\d+\;?'
    return t

def t_IF(t):
   r'if'
   return t

def t_ELSE(t):
    r'else'
    return t

def t_NULL(t):
   r'null'
   return t

def t_BREAK(t):
   r'break'
   return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_VAR(t):
    r'var'
    return t

def t_VOID(t):
   r'void'
   return t

def t_FOR(t):
    r'for'
    return t

def t_ID(t):
    r'\w+\=|\w+\s\='
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_STRING(t):
    r'\w+|:'
    return t

#REYES GUADALUPE KAUIL ESPADAS
#ELIEL DAVID NOVELO CAHUM
#MARCO ANTONIO BAEZA CAHUM
lexer = lex.lex()
