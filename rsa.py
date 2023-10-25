#!/usr/bin/python3

import sys


def factor(line):
    number = int(line)
    value = 0
    if number < 4:
        print("{:d}={:d}*1".format(number, number))
        return
    for i in range(2, number):
        if number % i == 0:
            value = number // i
            break
    print("{:d}={:d}*{:d}".format(number, value, i))


if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit()
filename = sys.argv[1]
try:
    test = open(filename, "r")
except FileNotFoundError:
    print("Error: Can't open file <{:s}>".format(filename))
    sys.exit()
line = test.read()
factor(line)

test.close()
