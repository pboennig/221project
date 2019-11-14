from truth_table import TruthTable
from oracle import oracle
from baseline import baseline
from gen_data import FormulaSource
from copy import copy
from formula import Formula
from neural_net import NeuralNet

NUM_TEST_FORMULAS = 100

nn = NeuralNet()
nn.train()
testFormulas = FormulaSource()
testFormulas.gen_data(NUM_TEST_FORMULAS)
numCorrect = 0
numTotal = 0
nnC = 0
for f in testFormulas.data:
    t = TruthTable(Formula(f))
    t.gen_table()

    oracle(t)
    oracleT = copy(t.table)

    baseline(t)
    baseT = copy(t.table)

    nn.solve_table(t)
    nnT = copy(t.table)
    for k in oracleT:
        numTotal += 1
        if oracleT[k] == baseT[k]:
            numCorrect += 1
        if oracleT[k] == nnT[k]:
            nnC += 1

print("Baseline: {}/{} correct".format(numCorrect, numTotal), "accuracy={}".format(numCorrect / numTotal))
print("NN: {}/{} correct".format(nnC, numTotal), "accuracy={}".format(nnC / numTotal))
