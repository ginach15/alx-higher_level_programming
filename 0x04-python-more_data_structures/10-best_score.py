#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
             k = list(a_dictionary.keys())
    o = sorted(a_dictionary.values())
    v = list(a_dictionary.values())
    vhi = o[-1]
    for no in range(len(v)):
        if v[no] == vhi:
            khi = k[no]
    return khi
