#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1
    else:
        num2 = number
    lastdigit = num2 % 10
    print(number % 10, end='')
    return (number % 10)
