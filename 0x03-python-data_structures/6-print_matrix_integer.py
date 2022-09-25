#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for data in matrix:
            for sub_data in data:
                print("{:d} ".format(sub_data), end='')
            print('')
