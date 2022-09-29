#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    if argv[2] in ["+","-","*","/"]:
        a = int(argv[1]), b = int(argv[3])
        if argv[2] == "+":
            print({:d} {} {:d} = {:d}).format(a, argv[2], b, add(a,b)))
        elif argv[2] == "-":
            print({:d} {} {:d} = {:d}).format(a, argv[2], b, sub(a,b)))
        elif argv[3] == "*":
            print({:d} {} {:d} = {:d}).format(a, argv[2], b, mul(a,b)))
        elif argv[2] == "/":
            print({:d} {} {:d} = {:d}).format(a, argv[2], b, div(a,b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            return 1



