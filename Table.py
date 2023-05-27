from Grammar import Grammar


class Table:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.table = {}

    def create_table(self):
        tabla = {}

        for left in self.grammar.rules:
            tabla[left] = {}
            for first in self.grammar.first[left]:

                if first == 'epsilon':
                    continue

                for rule_left in self.grammar.rules[left]:
                    if first in rule_left:
                        if first in tabla[left]:
                            print("Error: Ambiguedad")
                            return False

                        tabla[left][first] = rule_left

                if rule_left[0] in self.grammar.Nterminals:
                    if first in self.grammar.first[rule_left[0]]:
                        if first in tabla[left]:
                            print("Error: Ambiguedad")
                            return False

                        tabla[left][first] = (rule_left)

            if 'epsilon' in self.grammar.first[left]:
                for follow_left in self.grammar.follow[left]:
                    if follow_left in tabla[left]:
                        print("Error: Ambiguedad")
                        return False

                    tabla[left][follow_left] = ('epsilon')

        self.table = tabla
        return True

    def print_table(self):
        print("\n")
        for left, right in self.table.items():
            print(left, right, '\n')
