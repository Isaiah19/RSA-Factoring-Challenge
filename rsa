#!/usr/bin/python3
from sys import argv

with open(argv[1]) as f:
    for line in f:
        n = int(line)
        print("{:d}=".format(n), end="")
        if n % 2 == 0:
            print("{}*2".format(n//2))
            continue
        for i in range(3, n, 2):
            if n % i == 0:
                factor = n//i
                for j in range(3, factor, 2):
                    if factor % j == 0 or i % j == 0:
                        break
                print("{}*{}".format(factor, i))
                break
