#!/usr/bin/env python
from math import log


def max_line(data='data/base_exp.txt'):
    with open(data) as f:
        for i, line in enumerate(f):
            x, y = line.strip().split(',')
            yield log(int(x)) * int(y), i + 1


def main():
    highest = max(max_line())
    print(highest)


if __name__ == "__main__":
    main()
