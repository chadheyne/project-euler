#!/usr/bin/env python
from math import sqrt, floor


def chakravala(d):
    '''
        http://en.wikipedia.org/wiki/Chakravala_method
    '''
    an, k, x, y, a0 = 1, 1, 1, 0, sqrt(d)
    while k != 1 or y == 0:
        an = k * (an // k + 1) - an
        an = an - floor((an - a0) // k) * k
        x, y = (an * x + d * y) // abs(k), (an * y + x) // abs(k)
        k = (an ** 2 - d) // k
    yield x, y, d


def maximal_diophantine():
    for d in range(2, 1001):
        sq = d ** 0.5
        if sq.is_integer():
            continue
        yield from chakravala(d)


def main():
    maximal_x = max(maximal_diophantine(), key=lambda solution: solution[0])
    print(maximal_x)


if __name__ == "__main__":
    main()
