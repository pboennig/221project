class Formula:
    def __init__(self, formula):
        self.formula = formula

    def getTokens(self):
        return self.formula.split(" ")

    def getVars(self):
        v = set()
        for token in self.getTokens():
            if len(token) == 1 and str.isalpha(token):
                v.add(token)
        return v 
                
