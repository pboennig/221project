from truth_table import TruthTable
from oracle import oracle
from baseline import baseline
from gen_data import FormulaSource
from copy import copy
from formula import Formula
from neural_net import NeuralNet
import time
import json
from itertools import product

NUM_TEST_FORMULAS = 100

sizes = list(product(range(2, 10), repeat=3))
print(len(sizes))
architectures = [NeuralNet(size) for size in sizes]
for i, nn in enumerate(architectures):
    start = time.time()
    nn.train()
    print(i, time.time() - start)
scores = [0 for _ in architectures]

testFormulas = FormulaSource()
testFormulas.gen_data(NUM_TEST_FORMULAS)
numCorrect = 0
numTotal = 0
for f in testFormulas.data:
    t = TruthTable(Formula(f))

    oracle(t)
    oracleT = copy(t.table)

    baseline(t)
    baseT = copy(t.table)
    nn_tables = []
    for nn in architectures:
        nn.solve_table(t)
        nn_tables.append(copy(t.table))
    for k in oracleT:
        numTotal += 1
        if oracleT[k] == baseT[k]:
            numCorrect += 1
        for i, nnT in enumerate(nn_tables):
            if nnT[k] == oracleT[k]:
                scores[i] += 1

print("Baseline: {}/{} correct".format(numCorrect, numTotal), "accuracy={}".format(numCorrect / numTotal))
for i, score in enumerate(scores):
    print("NN{}: {}/{} correct".format(sizes[i], score, numTotal), "accuracy={}".format(score / numTotal))
with open('scores_dict.json', 'w') as f:
    json.dump({str(size):score for (size, score) in zip(sizes, scores)}, f)
    print('json complete')





