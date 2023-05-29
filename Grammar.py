import re


class Grammar:
    def __init__(self):
        self.rules = {}
        self.terminals = {}
        self.Nterminals = {}
        self.first = {}
        self.follow = {}
        self.start = None

    def _create_follow_Nterminal_End(self, element, left):
        for i in range(1, len(element)):
            if element[i-1] in self.Nterminals or element[i-1] in self.terminals:
                if element[i] in self.Nterminals:
                    if (i + 1) == len(element):
                        follow = self.follow[element[i]]
                        for key in follow.keys():
                            self.follow[left][key] = key

    def _create_follow_Nterminal_epsilon(self, element):
        for i in range(1, len(element)):
            if element[i-1] in self.Nterminals:
                if element[i] in self.Nterminals:
                    first = self.first[element[i]]
                    for key in first.keys():
                        if key == "epsilon":
                            follow = self.follow[element[i]]
                            for key in follow.keys():
                                self.follow[element[i-1]][key] = key

    def _create_follow_Nterminal_Nterminal(self, element):
        for i in range(1, len(element)):
            if element[i-1] in self.Nterminals:
                if element[i] in self.Nterminals:
                    first = self.first[element[i]]
                    for key in first.keys():
                        if key == "epsilon":
                            continue
                        self.follow[element[i-1]][key] = key

    def _create_follow_Nterminal_terminal(self, element):
        for i in range(1, len(element)):
            if element[i-1] in self.Nterminals:
                if element[i] in self.terminals:
                    self.follow[element[i-1]][element[i]] = element[i]

    def create_follow(self):
        for left in self.Nterminals:
            self.follow[left] = {}

        for i in range(3):
            for index, (left, right) in enumerate(self.rules.items()):
                if index == 0:
                    self.follow[left]["$"] = "$"
                for element in right:
                    self._create_follow_Nterminal_terminal(element)
                    self._create_follow_Nterminal_Nterminal(element)
                    self._create_follow_Nterminal_epsilon(element)
                    self._create_follow_Nterminal_End(element, left)

    def _create_first(self, Nterminal, left):
        productions = self.rules[Nterminal]
        for element in productions:
            if element == "epsilon":
                self.first[left][element] = element
            if element[0] in self.terminals:
                self.first[left][element[0]] = element[0]
            if element[0] in self.Nterminals:
                if element[0] == Nterminal:
                    continue

                if element[0] in self.first:
                    continue

                self._create_first(element[0], left)

    def create_first(self):
        for left, right in self.rules.items():
            if left not in self.first:
                self.first[left] = {}
            for element in right:
                if element == "epsilon":
                    self.first[left][element] = element
                if element[0] in self.terminals:
                    self.first[left][element[0]] = element[0]
                if element[0] in self.Nterminals:
                    self._create_first(element[0], left)

    def add_rule(self, left, right):
        if left not in self.rules:
            self.rules[left] = []
        self.rules[left] += right

    def add_terminals(self, right):
        for element in right:
            if element == "epsilon":
                continue
            caracter = re.findall("[a-z0-9\+\/\*\-\%\=\(\)]", element)
            for token in caracter:
                self.terminals[token] = token

    def add_Nterminals(self, left):
        self.Nterminals[left] = left
