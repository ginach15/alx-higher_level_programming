#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = list(a_dictionary.keys())
    v = list(a_dictionary.values())
    for i in range(len(v)):
        if value == v[i]:
            word = k[i]
            del a_dictionary[word]
    return a_dictionary
