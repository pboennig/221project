from truth_table import TruthTable
from oracle import oracle
from baseline import baseline
from gen_data import FormulaSource
from copy import copy
from formula import Formula

NUM_TEST_FORMULAS = 100

testFormulas = FormulaSource()
testFormulas.gen_data(NUM_TEST_FORMULAS)
numCorrect = 0
numTotal = 0
for f in testFormulas.data:
    t = TruthTable(Formula(f))
    t.gen_table()
    
    oracle(t)
    oracleT = copy(t.table)
    baseline(t)
    baseT = copy(t.table)

    for k in oracleT:
    	numTotal += 1
    	if oracleT[k] == baseT[k]:
    		numCorrect += 1

print("{}/{} correct".format(numCorrect, numTotal))