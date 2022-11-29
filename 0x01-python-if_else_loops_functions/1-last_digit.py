#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    num2 = number * -1
else:
    num2 = number
lastdig = num2 % 10
if (number < 0):
    lastdig = lastdig * -1
if (lastdig == 0):
    print("Last digit of {:d} is 0 and is 0".format(number))
elif (lastdig > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(
    number, lastdig))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
    number, lastdig))
