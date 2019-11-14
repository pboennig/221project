from formula import Formula
from truth_table import TruthTable
from baseline import baseline

while True:
    usr = input("Type a formula or <enter> to quit: ")
    if usr == '': break
    f = Formula(usr)
    print("Formula:", f.formula)
    t = TruthTable(f.getVars())
    t.gen_table()
    print("Empty table:")
    t.print_table()
    print("\nBaseline:")

    baseline(t)
    t.print_table()

