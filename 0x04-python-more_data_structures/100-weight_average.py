#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    w = 0
    sw = 0
    for items in range(len(my_list)):
        t = my_list[items]
        w += t[1]
        sw += t[0] * t[1]
    wa = float(sw / w)
    return 
