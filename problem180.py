#!/usr/bin/env python
from fractions import Fraction
from utils.decorators import timeit


def calc_g(x, y):
    z = x + y
    a, b = int(z.numerator ** 0.5), int(z.denominator ** 0.5)
    if a ** 2 == z.numerator and b ** 2 == z.denominator:
        return Fraction(a, b)
    return Fraction(-1)


@timeit
def solve_it(limit=35):
    s, n = set(), set()
    n = set([Fraction(a, b) for a in range(1, limit) for b in range(a + 1, limit + 1)])

    for x in n:
        for y in n:
            zs = (x + y,
                  calc_g(x ** 2, y ** 2),
                  (x ** -1 + y ** -1) ** -1,
                  calc_g(x ** -2, y ** -2) ** -1)
            zs = (x + y + z for z in zs if z in n)

            s.update(set(zs))

    t = sum(s)
    return t.denominator + t.numerator


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))


if __name__ == "__main__":
    main()
