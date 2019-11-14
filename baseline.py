def baseline(t):
    for entry in t.table:
        e = list(entry)
        true_count = len([x for x in e if x.b])
        if true_count > len(e) / 2:
            t.table[entry] = 1
        else:
            t.table[entry] = 0 

