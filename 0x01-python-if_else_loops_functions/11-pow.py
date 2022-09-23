#!/usr/bin/python3
def pow(a, b):
    x = 1
    if b < 0:
        n = b * -1
    else:
        n = b
    for i in range(n):
        x = x * a
    if(b < 0):
        return 1 / x
    else:
        return x
