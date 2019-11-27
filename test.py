from formula import Formula
from truth_table import TruthTable
from oracle import oracle
from baseline import baseline
from neural_net import NeuralNet

nn = NeuralNet()
nn.train()

def get_user_input():
    usr = input("Type a formula or <enter> to quit: ")
    usr = usr.replace('(', ' ( ')
    usr = usr.replace(')', ' ) ')
    usr = usr.replace('if', '( not')
    usr = usr.replace('then', ') or')
    return ' '.join(usr.split())

while True:
    usr = get_user_input()
    if usr == '': break

    f = Formula(usr)
    print("Formula:", f.formula)
    t = TruthTable(f)
    
    print("Oracle:")
    oracle(t)
    t.print_table()
    print("Baseline:")
    baseline(t)
    t.print_table()
    print("NeuralNet:")
    nn.solve_table(t)
    t.print_table()


