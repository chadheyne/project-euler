#!/usr/bin/env python
from fractions import Fraction
import sys


def continued_frac(start=Fraction(1, 3), end=Fraction(1, 2), limit=12000):
    if start.denominator + end.denominator <= limit:
        mediant = Fraction(start.numerator + end.numerator,
                           start.denominator + end.denominator)
        yield from continued_frac(start, mediant)
        yield from continued_frac(mediant, end)
    elif start != Fraction(1, 3):
        yield start


def main():
    sys.setrecursionlimit(7500)
    between = sum(1 for frac in continued_frac())
    print(between)

if __name__ == "__main__":
    main()
