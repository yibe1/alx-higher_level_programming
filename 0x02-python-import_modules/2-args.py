#!/usr/bin/python3
if __name__ == "__main__":
    size = len(argv)
    if size == 1:
        print("{} argument:".format(i))
    else:
        if size == 0:
            print("{} arguments.".format(i))
        else:
            print("{} arguments:".format(i))
    for i in range(size):
        print("{:d:} {}".format(i + 1, argv[i]))
