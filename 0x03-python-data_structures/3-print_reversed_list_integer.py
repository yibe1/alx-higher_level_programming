#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        i = len(my_list) - 1
        for data in my_list:
            print("{:d}".format(my_list[i]))
            i -= 1
    else:
        return None
