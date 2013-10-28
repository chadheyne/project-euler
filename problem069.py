#!/usr/bin/env python
from functools import reduce
from operator import mul

PRIMES = {int(i) for i in open('data/primes.txt').readlines() if int(i) < 1000}


def find_factors(number):
    for p in PRIMES:
        if number % p == 0:
            yield (1 - 1 / p)
        if p > number:
            break


def totient(upper_bound=1000000):
    for n in range(2, upper_bound + 1):
        if n in PRIMES:
            continue
        else:
            yield n, int(reduce(mul, find_factors(n), n))


def easy_way(limit=1000000):
    result = 1
    primes = iter(int(i) for i in open('data/primes.txt').readlines() if int(i) < 5000)
    for n in primes:
        if result * n > limit:
            return result
        result *= n


def main():
    largest = max(totient(), key=lambda n: n[0] / n[1])
    #largest = easy_way()
    print(largest)


if __name__ == "__main__":
    main()
