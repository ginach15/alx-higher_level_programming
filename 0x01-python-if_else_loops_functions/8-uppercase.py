#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if ((x >= 97) and (x <= 122)):
            y = chr(x - 32)
        else:
            y = str[i]
        print("{}".format(y), end='')
    print("")
