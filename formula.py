class Formula:
    def __init__(self, formula):
        self.formula = formula

    def getTokens(self):
        return self.formula.split()

    def getVars(self):
        variables = []
        for token in self.getTokens():
            if token not in {'(', ')', 'not', 'and', 'or'} \
                    and token not in variables:
                variables.append(token)
        return variables 
                
