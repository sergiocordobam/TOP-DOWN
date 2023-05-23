from Grammar import Grammar


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
    print('\n')
    print(grammar.first, '\n')
    print(grammar.follow)
    return grammar


read_grammar()
