#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    k = list(a_dictionary.keys())
    for i in range(0, len(a_dictionary)):
        word = k[i]
        newdict[word] = a_dictionary.get(word) * 2
    return newdict
