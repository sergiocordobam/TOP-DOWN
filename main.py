from Grammar import Grammar
from Table import Table


def read_grammar():
    grammar = Grammar()
    line = input().split(" ")
    str1 = ""
    line = str1.join(line)
    while line:
        left, right = line.split('->')
        right = right.split("|")
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
table.create_table()
table.print_table()
