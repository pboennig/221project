import formula

def oracle(t):
    """
    Given a truth table t, populates t with the
    actual truth values of t's formula under all
    possible variable assignments.

    param t: instance of the TruthTable class
    """
    for entry in t.table:
        model = {e.v: e.b for e in entry}
        t.table[entry] = getTruthVal(t.formula, model)

def getTruthVal(formula, model):
    """
    Given a formula and a model containing assignments
    to all the variables in the formula, returns the
    truth value of the formula under the model.

    param formula: instance of the Formula class
    param model: dict of variable: assignment pairs
    """
    tokens = formula.getTokens()
    def recurse(i):
        while i < len(tokens) and tokens[i] != ')':
            if tokens[i] in model:
                soFar = model[tokens[i]]
                i += 1
            else:
                val, iNext = recurse(i + 1)
                if tokens[i] == '(':
                    soFar = val
                    iNext += 1
                elif tokens[i] == 'not':
                    soFar = not val
                elif tokens[i] == 'and':
                    soFar = soFar and val
                elif tokens[i] == 'or':
                    soFar = soFar or val
                i = iNext
        return soFar, i
    return 1 if recurse(0)[0] else 0

