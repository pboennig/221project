"""
File that defines a truth table. Generates the row labels automatically based
on the variables and initializes the values in the map to none.
"""
class Entry:
    def __init__(self, v, b):
        self.v = v
        self.b = b

    def __repr__(self):
        return "({}, {})".format(self.v, self.b)
class TruthTable:
    def __init__(self, variables):
        self.variables = variables
        self.n = len(variables)
        self.table = {}

    def gen_table(self):
        entries = [[] for _ in range(2**self.n)]
        s = int(len(entries) / 2)
        for v in self.variables:
            n = 0
            while n < len(entries):
                for _ in range(s):
                    entries[n].append(Entry(v, True))
                    n += 1
                for _ in range(s):
                    entries[n].append(Entry(v, False))
                    n += 1
            s = int(s / 2)

        for entry in entries:
            self.table[tuple(entry)] = None 
        print(self.table)

    def print_table(self):
        for entry in self.table:
            print(entry, ":", self.table[entry])

