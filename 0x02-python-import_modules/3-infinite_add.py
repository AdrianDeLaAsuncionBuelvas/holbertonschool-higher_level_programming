#!/usr/bin/python3
import sys
from sys import argv
if (__name__ == '__main__'):
    sum = 0
    if (len(argv) == 1):
        print("0")
    if (len(argv) > 1):
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{:d}".format(sum))
