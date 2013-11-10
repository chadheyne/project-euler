#!/usr/bin/env python
from math import log
from fractions import gcd
from utils.decorators import timeit


def func(n, k):
    return k * log(n/k)


def fun(n):
    i1, i2 = 1, n
    while i2 - i1 > 1:
        i3 = (i1 + i2) // 2
        if func(n, i3) < func(n, i3 + 1):
            i1 = i3
        else:
            i2 = i3
    return i2


def is_positive(n):
    denom = fun(n)
    _gcd = gcd(n, denom)
    denom /= _gcd
    while not denom % 2:
        denom //= 2
    while not denom % 5:
        denom //= 5
    return n if denom != 1 else -1 * n


@timeit
def solve_it(limit=10000):
    return sum(is_positive(i) for i in range(5, limit+1))


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))


if __name__ == "__main__":
    main()
