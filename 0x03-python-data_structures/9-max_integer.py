#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if(my_list):
        if len(my_list) == 0:
            return None
        else:
            max = my_list[0]
        for i in range(len(my_list)):
            if max < my_list[i]:
                max = my_list[i]
    else:
        return None
    return max
