#!/usr/bin/env python
from math import sqrt, ceil
from itertools import starmap
from functools import reduce
from operator import mul
from utils.decorators import timeit


def find_factors(start):
    if start <= 1:
        return
    prime = next((x for x in range(2, ceil(sqrt(start) + 1)) if not start % x), start)
    yield prime
    yield from find_factors(start//prime)


@timeit
def solve_it(target=47547):
    factors = list(find_factors(target * 2 + 1))[::-1]
    first_primes = [2, 3, 5, 7, 11]
    a_terms = [n // 2 if i > 0 else n // 2 + 1 for i, n in enumerate(factors)]
    answer = reduce(mul, starmap(pow, zip(first_primes, a_terms)))
    return answer


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))


if __name__ == "__main__":
    main()
