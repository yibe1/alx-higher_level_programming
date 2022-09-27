#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    size = len(argv)
    if size == 2:
        print("{} argument:".format(1))
    else:
        if size < 2:
            print("{} arguments.".format(0))
        else:
            print("{} arguments:".format(size - 1))
    for i in range(1, size):
        print("{:d}: {}".format(i, argv[i]))
