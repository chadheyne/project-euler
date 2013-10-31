#!/usr/bin/env python
from math import sqrt, ceil
from functools import reduce
from operator import mul


def find_factors(start):
    if start <= 1:
        return
    prime = next((x for x in range(2, ceil(sqrt(start) + 1)) if not start % x), start)
    yield prime
    yield from find_factors(start//prime)


def radicals(limit=100000):
    results = [(0, 0), (1, 1)]
    for number in range(2, limit+1):
        results.append((reduce(mul, set(find_factors(number))), number))

    return sorted(results)[10000]


def main():
    answer = radicals()
    print(answer)


if __name__ == "__main__":
    main()
