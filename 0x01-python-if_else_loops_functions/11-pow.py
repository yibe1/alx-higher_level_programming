#!/usr/bin/python3
def pow(a, b):
    x = 1
    for i in range(b):
        x = x * a
    if(b < 0):
        return 1 / x
    else:
        return x
