#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    if my_list:
        new_list = []
        for data in my_list:
            new_list.append(data)
        new_list[idx] = element
        return new_list

            
