from Table import Table


class Lexer:
    def __init__(self, table: Table, input: str):
        self.table = table
        self.stack = []
        self.input = input + '$'

    def analyze_input(self):
        self.stack.append('$')
        self.stack.append(self.table.grammar.start)

        first_stack = self.stack[-1]
        first_input = self.input[0]

        while self.stack:
            if first_stack == '$' and first_input == '$':
                return True

            # If the first element of the stack is equal to the first element of the input
            if first_stack == first_input:
                self.stack.pop()
                first_stack = self.stack[-1]
                # if len(self.input) != 1:
                self.input = self.input[1:]
                first_input = self.input[0]
                continue

            if first_stack in self.table.grammar.Nterminals:
                if first_input not in self.table.table[first_stack]:
                    return False

                prodcution = self.table.table[first_stack][first_input]
                self.stack.pop()
                for i in range(len(prodcution)):
                    self.stack.append(prodcution[len(prodcution) - i - 1])

                first_stack = self.stack[-1]

            else:
                return False
