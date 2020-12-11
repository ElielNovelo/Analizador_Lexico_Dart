import sys
from lexico_dart import lexer
n=0
if __name__ == "__main__":
    file_name = 'prueba.dart'
    file = open(file_name, "r")
    data = file.read()
    lexer.input(data)

    while True:
        n=n+1
        tok = lexer.token()
        if not tok:
            break
        print ("Token ",n," >>>> ", tok)