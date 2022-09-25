#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    i = len(my_list) - 1
    for data in my_list:
        print("{:d}".format(my_list[i]))
        i -= 1
