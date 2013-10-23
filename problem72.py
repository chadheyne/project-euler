#!/usr/bin/env python
from operator import mul
from functools import reduce
from decimal import Decimal

with open('data/primes.txt') as f:
    PRIMES = []
    for num in f:
        if int(num) > 1000000:
            break
        PRIMES.append(int(num))


def find_factors(number):
    for p in PRIMES:
        if number % p == 0:
            yield (1 - Decimal(1) / Decimal(p))
        if p > number:
            break


def farey_length(limit=1000000, baseline=0):
    for number in range(2, limit + 1):
        baseline += int(reduce(mul, find_factors(number), number))
    return baseline


def main():
    sequence = farey_length()
    print(sequence)


if __name__ == "__main__":
    main()
