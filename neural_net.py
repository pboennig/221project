from oracle import oracle, getTruthVal
from baseline import baseline
from gen_data import FormulaSource
from copy import copy
from formula import Formula
from truth_table import TruthTable
from sklearn.neural_network import MLPClassifier

class NeuralNet:
    def __init__(self):
        N = 1000
        percent_train = .8
        fs = FormulaSource()
        fs.gen_data(N)
        split = int(len(fs.data) * percent_train)
        train_data = list(fs.data)[:split]
        test_data = list(fs.data)[split:]
        self.X_train, self.Y_train = self.label_data(train_data)
        self.X_test, self.Y_test = self.label_data(test_data)       
        self.clf = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(10,5), warm_start=True, max_iter=1000)

    def label_data(self, data):
        X = []
        Y = []
        for s in data:
            f = Formula(s)
            tt = TruthTable(f)
            tt.gen_table()
            oracle(tt)
            for entry in tt.table:
                w = {e.v : e.b for e in entry}
                X.append(self.featurize(f, w))
                Y.append(tt.table[entry])
        return X, Y

    def featurize(self, f, w):
        numTrue = sum(w[v] for v in w)
        numVars = len(w)
        numOr, numNot, numAnd = (0, 0, 0)
        for t in f.getTokens():
            if t == 'or':
                numOr += 1
            elif t == 'not':
                numNot += 1
            elif t == 'and':
                numAnd += 1

        return [numVars, numOr, numNot, numAnd, numTrue]
    
    def train(self):
        self.clf.fit(self.X_train, self.Y_train)

    def solve_table(self, tt):
        for entry in tt.table:
            model = {e.v: e.b for e in entry}
            tt.table[entry] = self.classify(tt.formula, model)

    '''
    Intepretation function for neural network.
    '''
    def classify(self, f, w):
        return self.clf.predict([self.featurize(f, w)])[0]





