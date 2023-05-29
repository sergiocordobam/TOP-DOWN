from Table import Table


class Lexer:
    def __init__(self, table: Table, input: str):
        self.table = table
        self.pila = []
        self.input = input + '$'

    def verificar_entrada(self):
        self.pila.append('$')
        self.pila.append(self.table.grammar.start)

        first_stack = self.pila[-1]
        first_input = self.input[0]

        while self.pila:
            if first_stack == '$' and first_input == '$':
                return True

            if first_stack == first_input:
                self.pila.pop()
                first_stack = self.pila[-1]
                self.input = self.input[1:]
                first_input = self.input[0]
                continue

            if first_stack in self.table.grammar.Nterminals:
                if first_input not in self.table.table[first_stack]:
                    return False

                production = self.table.table[first_stack][first_input]
                self.pila.pop()
                for i in range(len(production)):
                    self.pila.append(production[len(production) - i - 1])

                first_stack = self.pila[-1]

            else:
                return False
