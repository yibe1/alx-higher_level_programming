#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0;
    for data in matrix:
        for sub_data in data:
            print("{:d}".format(sub_data), end='')
            if i != len(data)-1:
                print(" ", end='')
        print('')
