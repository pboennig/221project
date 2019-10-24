from formula import Formula
from truth_table import TruthTable
from baseline import baseline

f = Formula("( not P ) and Q and R")
t = TruthTable(f.getVars())
t.gen_table()

baseline(t)
t.print_table()
