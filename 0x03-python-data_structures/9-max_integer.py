#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
    for i in range(len(my_list) - 1):
        if max < my_list[i]:
            max = my_list[i]
    return max
