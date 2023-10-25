#!/usr/bin/python3
from sys import argv
from math import sqrt
def factor(n):
    if n % 2 == 0:
        yield 2
        while n % 2 == 0:
            n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            yield i
            while n % i == 0:
                n //= i
    if n > 2:
        yield n


with open(argv[1]) as f:
    for line in f:
        n = int(line)
        print("{:d}=".format(n), end="")
        if n % 2 == 0:
            print("{}*2".format(n//2))
            continue
        for i in factor(n):
            print("{}*{}".format(n//i, i))
            break
        print()
