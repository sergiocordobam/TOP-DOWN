import re


class Grammar:

    def __init__(self):
        self.rules = {}
        self.terminals = {}
        self.Nterminals = {}
        self.first = {}
        self.follow = {}
    
    def _create_follow_Nterminal_End(self, token, left):
        for i, s in enumerate(token):
            if s in self.Nterminals or s in self.terminals:
                if i >= len(token) - 1:
                    continue

                if token[i + 1] in self.Nterminals:

                    if (i+2) == len(token):
                        follow = self.follow[token[i + 1]]
                        for key, value in follow.items():
                            self.follow[left][key] = value

    def _create_follow_Nterminal_epsilon(self, token, left):
        for i, s in enumerate(token):
            if s in self.Nterminals:
                if i >= len(token) - 1:
                    continue

                if token[i + 1] in self.Nterminals:
                    first = self.first[token[i + 1]]

                    for key, value in first.items():
                        if key == "epsilon":
                            follow = self.follow[token[i + 1]]
                            for key, value in follow.items():
                                self.follow[s][key] = value

    def _create_follow_Nterminal_Nterminal(self, token, left):
        for i, s in enumerate(token):
            if s in self.Nterminals:
                if i >= len(token) - 1:
                    continue

                if token[i + 1] in self.Nterminals:
                    first = self.first[token[i + 1]]
                    for key, value in first.items():
                        if key == "epsilon":
                            continue
                        self.follow[s][key] = value

    def _create_follow_Nterminal_terminal(self, token):
        for i, s in enumerate(token):
            if s in self.Nterminals:
                if i >= len(token) - 1:
                    continue
                if token[i + 1] in self.terminals:
                    self.follow[s][token[i + 1]] = token[i + 1]

    def create_follow(self):
        for left in self.Nterminals:
            self.follow[left] = {}

        for i in range(3):
            for index, (left, rights) in enumerate(self.rules.items()):
                if index == 0:
                    self.follow[left]["$"] = "$"
                for tokens in rights:
                    for token in tokens:
                        self._create_follow_Nterminal_terminal(token)
                        self._create_follow_Nterminal_Nterminal(token, left)
                        self._create_follow_Nterminal_epsilon(token, left)
                        self._create_follow_Nterminal_End(token, left)

    def _create_first(self, Nterminal, left):
        rules = self.rules[Nterminal]
        for tokens in rules:
            for token in tokens:
                if token == "epsilon":
                    self.first[left][token] = token
                if token[0] in self.terminals:
                    self.first[left][token[0]] = token[0]
                if token[0] in self.Nterminals:

                    if token[0] == Nterminal:
                        continue

                    if token[0] in self.first:
                        continue

                    self._create_first(token[0], left)

    def create_first(self):
        for left, rights in self.rules.items():
            if left not in self.first:
                self.first[left] = {}
            for tokens in rights:
                for token in tokens:
                    if token == "epsilon":
                        self.first[left][token] = token
                    if token[0] in self.terminals:
                        self.first[left][token[0]] = token[0]
                    if token[0] in self.Nterminals:
                        self._create_first(token[0], left)

    def add_rule(self, left, right):
        if left not in self.rules:
            self.rules[left] = []
        self.rules[left].append(right)

    def add_terminals(self, right):
        for element in right:
            if element == "epsilon":
                continue
            hlp = re.findall("[a-z0-9\+\/\*\-\%\=\(\)]", element)
            for token in hlp:
                self.terminals[token] = token

    def add_Nterminals(self, left):
        self.Nterminals[left[0]] = left[0]

    def __str__(self):
        result = ''
        for left, rights in self.rules.items():
            for right in rights:
                result += f"{left} -> {' | '.join(right)}\n"
        return result
