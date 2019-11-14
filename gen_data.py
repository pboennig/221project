import random

class FormulaSource:
    def __init__(self):
        self.vars = ['P', 'Q', 'R', 'S']
        self.binary = ['and', 'or']
        self.unary = ['not']
        self.data = set()
     
    def gen_formula(self):
        new_token = random.choice(self.vars) 
        split = random.randint(0, 2)
        if split == 0:
            return new_token
        elif split == 1:
            new_token = 'not ' + new_token
        elif split == 2:
            new_token = new_token + ' ' + random.choice(self.binary) + ' ' + self.gen_formula()
        return '( ' + new_token + ' )'


    def gen_data(self, N):
        for _ in range(N):
            self.data.add(self.gen_formula())

fs = FormulaSource()
fs.gen_data(10)
print(list(fs.data))
