#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list == None:
        return None
    else:
        max = my_list[0]
    for i in my_list:
        if max < my_list[i]:
            max = my_list[i]
    return max
