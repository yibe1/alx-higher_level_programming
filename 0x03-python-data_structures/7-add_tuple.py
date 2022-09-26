#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()): 
    a = 0
    b = 0
    n11 = 0
    n12 = 0
    n21 = 0
    n22 = 0
    
    if len(tuple_a) > 0:
        n11 = tuple_a[0]
    if len(tuple_a) > 1:
        n12 = tuple_a[1]
    if len(tuple_b) > 0:
        n21 = tuple_b[0]
    if len(tuple_b) > 1:
        n22 = tuple_b[1]
    new_tuple = (n11 + n21, n12 + n22)
    return new_tuple
