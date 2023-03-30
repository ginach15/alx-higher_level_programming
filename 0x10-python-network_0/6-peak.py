#!/usr/bin/python3
"""
module has find_peak function that finds a peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """returns a peak in a list of unsorted integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    # see if the ends are peaks
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    # peak is not at either end
    else:
        middle = len(list_of_integers) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            return find_peak(list_of_integers[middle:])
        elif list_of_integers[middle] < list_of_integers[middle - 1]:
            return find_peak(list_of_integers[:middle])
        else:
            return list_of_integers[middle]
