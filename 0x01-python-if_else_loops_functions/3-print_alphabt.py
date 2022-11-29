#!/usr/bin/python3
for az in range(97, 123):
    if ((az == 101) or (az == 113)):
        continue
    print("{}".format(chr(az)), end='')
