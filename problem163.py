#!/usr/bin/env python
from utils import decorators
from math import floor


def trinomial(a, b, c, n):

    return a * pow(n, 3) + b * pow(n, 2) + c * n


@decorators.timeit
def closed_form(n=36):
    term1 = floor(trinomial(2, 5, 2, n) / 8) + 2 * floor(trinomial(1, 0, -1 / 3, n) / 2)
    term2 = (6 * (n * (n + 1) * (n + 2) / 6 +
             floor(trinomial(2, 5, 2, n) / 8) +
             floor(trinomial(2, 3, -3, n) / 18) +
             floor(trinomial(2, 3, -3, n) / 10)))
    term3 = 3 * floor((trinomial(22, 45, -4, n) / 48))
    return int(term1 + term2 + term3)


def main():
    answer, time = closed_form()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))

if __name__ == "__main__":
    main()
