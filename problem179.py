#!/usr/bin/env python
from math import sqrt
from utils.decorators import timeit


@timeit
def solve_it(limit=10**7):
    factors = [2] * (limit + 1)
    for i in range(2, int(sqrt(limit))):
        j = pow(i, 2)
        factors[j] -= 1
        while j <= limit:
            factors[j] += 2
            j += i
    return sum(1 for i in range(2, limit - 1) if factors[i] == factors[i+1])


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))


if __name__ == "__main__":
    main()
