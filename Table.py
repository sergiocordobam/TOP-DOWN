from Grammar import Grammar

class Table:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.table = {}

    def create_table(self):
        tabla = {}
        productions = {}
        for left, right in self.grammar.rules.items():
            A = right[0]
            productions[left] = A

        print(productions)
        print(self.grammar.first,'\n','\n')
        
        for A in productions:
            tabla[A] = {}
            for a in self.grammar.first[A]:

                for b in productions[A]:
                    if a in b:
                        tabla[A][a] = b
                
                if b[0] in self.grammar.Nterminals:
                    if a in self.grammar.first[b[0]]:
                        tabla[A][a] = b


            if 'epsilon' in self.grammar.first[A]:
                for b in self.grammar.follow[A]:
                    tabla[A][b] = productions[A]

        self.table = tabla
    
    def print_table(self):
        for left, right in self.table.items():
            print(left, right, '\n')
