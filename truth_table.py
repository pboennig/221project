"""
File that defines a truth table. Generates the row labels automatically based
on the variables and initializes the values in the map to none.
"""

from itertools import product

class Entry:
    def __init__(self, v, b):
        self.v = v
        self.b = b

    def __repr__(self):
        return "({}, {})".format(self.v, self.b)

class TruthTable:
    def __init__(self, formula):
        self.formula = formula
        self.variables = formula.getVars()
        self.n = len(self.variables)
        self.gen_table()

    def gen_table(self):
        self.table = {}
        for values in product((1, 0), repeat=self.n):
            entry = tuple(Entry(var, val) for var, val \
                          in zip(self.variables, values))
            self.table[entry] = None

    def print_table(self):
        print(' '.join(self.variables), '| Evaluation')
        for entry, evaluation in self.table.items():
            assignments = ''
            for i in range(self.n):
                assignments += str(entry[i].b)
                assignments += ' ' * len(self.variables[i])
            print('{}| {}'.format(assignments, self.table[entry]))

