#!/usr/bin/env python
from math import sqrt, floor


def continued_fractions(highest=10000):
    '''
        Algorithm from http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    '''
    for n in range(1, highest+1):
        m, d = 0, 1
        a0 = a = floor(sqrt(n))
        if a0 ** 2 == n:
            continue
        period = []
        while a != 2 * a0:
            m = d * a - m
            d = (n - m ** 2) / d
            a = floor((a0 + m) / d)
            period.append(a)
        yield len(period) % 2


def main():
    fractions = sum(1 for period in continued_fractions() if period)
    print(fractions)

if __name__ == "__main__":
    main()
