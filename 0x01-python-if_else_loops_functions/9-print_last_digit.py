#!/usr/bin/python3
def print_last_digit(number):
    x = int(repr(number)[-1])
    if(number < 0):x = x * -1
    print("{}".format(x),end='')
    return x
