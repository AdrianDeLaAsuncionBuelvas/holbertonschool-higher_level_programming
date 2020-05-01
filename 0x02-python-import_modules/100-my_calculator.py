#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == '__main__'):
    argc = len(argv) - 1
    operators = {'+', '-', '*', '/'}
    if (argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if (argv[2] == '+'):
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif (argv[2] == '-'):
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif (argv[2] == '*'):
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif (argv[2] == '/'):
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
