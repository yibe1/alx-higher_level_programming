#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    size = len(argv)
    if size == 1:
        print("{} argument:".format(1))
    else:
        if size == 0:
            print("{} arguments.".format(0))
        else:
            print("{} arguments:".format(size))
    for i in range(1, size):
        print("{:d}: {}".format(i, argv[i]))
