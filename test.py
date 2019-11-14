from formula import Formula
from truth_table import TruthTable
from oracle import oracle
from baseline import baseline

while True:
    usr = input("Type a formula or <enter> to quit: ")
    if usr == '': break
    f = Formula(usr)
    print("Formula:", f.formula)
    t = TruthTable(f)
    t.gen_table()
    print("Oracle:")
    oracle(t)
    t.print_table()
    print("Baseline:")
    baseline(t)
    t.print_table()

