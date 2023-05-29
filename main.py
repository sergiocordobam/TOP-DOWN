from Grammar import Grammar
from Table import Table
from Lexer import Lexer


def read_grammar():
    print("Ingrese una gramatica")
    grammar = Grammar()
    line = input().split(" ")
    str1 = ""
    line = str1.join(line)
    while line:
        left, right = line.split('->')
        right = right.split("|")
        if grammar.start is None:
            grammar.start = left
        grammar.add_rule(left, right)
        grammar.add_terminals(right)
        grammar.add_Nterminals(left)
        line = input().split(" ")
        str1 = ""
        line = str1.join(line)

    grammar.create_first()
    grammar.create_follow()

    return grammar


grammar = read_grammar()
print("First: ", grammar.first)
print("Follow: ", grammar.follow)
table = Table(grammar)
isLL1 = table.create_table()
print("Tabla LL(1): ")
table.print_table()
print("¿La gramática es LL(1)? :", isLL1)
if not isLL1:
    pass
else:
    while True:
        print("Ingrese una cadena para analizar: ")
        cadena_por_analizar = input()
        if cadena_por_analizar == "":
            break
        else:
            lexer = Lexer(table, cadena_por_analizar)
            isCorrect = lexer.verificar_entrada()
            if not isCorrect:
                print("no")
            else:
                print("si")

