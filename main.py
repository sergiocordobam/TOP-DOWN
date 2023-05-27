from Grammar import Grammar
from Table import Table
from Lexer import Lexer


def read_grammar():
    print("Ingrese la gramatica")
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
table = Table(grammar)
isLL1 = table.create_table()
if not isLL1:
    print("error")

else:
    print("Ingrese la cadena a analizar")
    string = input()
    while string:
        lexer = Lexer(table, string)
        isCorrect = lexer.analyze_input()
        if not isCorrect:
            print("no")
        else:
            print("si")
        string = input()
