#!/usr/bin/env python
from math import factorial
from functools import reduce
from operator import mul
from utils import decorators


def falling_factorial(x, n):
    return reduce(mul, (x - i for i in range(0, n)))


def n_choose_k(n, k):
    return falling_factorial(n, k) // factorial(k)


@decorators.timeit
def solve_it(limit=26):
    return max((2 ** i - i - 1) * n_choose_k(26, i) for i in range(1, limit+1))


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {}".format(answer, time))


if __name__ == "__main__":
    main()
