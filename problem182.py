#!/usr/bin/env python
from fractions import gcd
from utils.decorators import timeit


@timeit
def solve_it(p=1009, q=3643):
    n, phi = p * q, (p - 1) * (q - 1)
    maxn = pow(2, 63)
    elements = [e for e in range(11, phi, 12) if gcd(e, phi) == 1]
    total_e = [0] * (elements[-1] + 1)
    for el in elements:
        curtot = (1 + gcd(el - 1, p - 1)) * (1 + gcd(el - 1, q - 1))
        if curtot <= maxn:
            maxn = curtot
            total_e[el] = curtot
    return sum(i for i, n in enumerate(total_e) if n == maxn)


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))


if __name__ == "__main__":
    main()
