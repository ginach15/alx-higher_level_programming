#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0

    for i in range(0, x):
        try:
            print(my_list[i], end="")
            total += 1
        except IndexError:
            print("".format(), end="")
    print("".format())
    return total
