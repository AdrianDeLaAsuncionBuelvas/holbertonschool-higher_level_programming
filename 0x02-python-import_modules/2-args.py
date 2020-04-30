#!/usr/bin/python3
import sys
from sys import argv
if (__name__ == '__main__'):
    if (len(argv) == 1):
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif (len(argv) == 2):
        print("{:d} argument:".format(len(sys.argv) - 1))
    elif(len(argv) > 1):
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
