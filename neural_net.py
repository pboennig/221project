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
        split = len(fs.data) * percent_train
        train_data = list(fs.data)[:split]
        test_data = list(fs.data)[split:]
        X_train, Y_train = label_data(train_data)
        X_test, Y_test = label_data(test_data)

    def label_data(self, data):
        X = []
        Y = []
        for f in data:
            tt = TruthTable(formula)
            for entry in tt.table:
                w = {e.v : e.b for e in entry}
                X.append(self.featurize(f, w))
                Y.append(getTruthVal(f, w))

        return X, Y

    def
            


