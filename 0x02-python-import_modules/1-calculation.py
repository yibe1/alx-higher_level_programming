#!/usr/bin/python3
from calculator_1 as tk import add, sub, mul, div

def main():
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, tk.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, tk.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, tk.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, tk.div(a, b)))
if __name__ == "__main__":
    main()



